import subprocess
#file_name = ''
#file_name = input("Enter the smart contract file name ")
#sol_contract  ="./solc/"+ file_name
#file = file_name.replace(".sol", ".json")
#FILE = "./json/" + file



#with open(FILE, 'w') as f:
#   p1 = subprocess.run(['myth', 'analyze', sol_contract,'-o', 'json'], stdout=f, text=True)


def analyze_mythril(file_name):
    sol_contract  ="./solc/"+ file_name
    file = file_name.replace(".sol", ".json")
    FILE = "./json/" + file
    with open(FILE, 'w') as f:
        p1 = subprocess.run(['myth', 'analyze', sol_contract,'-o', 'json'], stdout=f, text=True)


    
    
analyze_mythril("force.sol")