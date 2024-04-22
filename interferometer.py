import strawberryfields as sf
from strawberryfields import ops
from math import pi

common_phases = [0, pi/2, pi, 3*pi/2, 2*pi]
state_preparations = ['Single Photon State', 'Coherent State']

def get_input():
    print("This program simulates a Mach-Zehnder interferometer with two input modes and two output modes.")
    print("You will be asked to choose the phase settings for each mode and the initial state preparation.")
    print()

    print("Choose from the following common phase settings:")
    for i, phase in enumerate(common_phases):
        print(f"{i}: Phase = {phase}")
    
    while True:
        try:
            choice = int(input("Enter the number of your choice for the phase in the first mode: "))
            if 0 <= choice < len(common_phases):
                phase1 = common_phases[choice]
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    while True:
        try:
            choice = int(input("Enter the number of your choice for the phase in the second mode: "))
            if 0 <= choice < len(common_phases):
                phase2 = common_phases[choice]
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    print()
    print("Choose from the following state preparations:")
    for i, state in enumerate(state_preparations):
        print(f"{i}: {state}")
    
    while True:
        try:
            choice = int(input("Enter the number of your choice for state preparation: "))
            if 0 <= choice < len(state_preparations):
                state_preparation = state_preparations[choice]
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    return phase1, phase2, state_preparation

def main():
    phase1, phase2, state_preparation = get_input()
    
    prog = sf.Program(2)
    
    with prog.context as q:
        # Prepare the chosen state in the first mode
        if state_preparation == 'Single Photon State':
            ops.Fock(1) | q[0]
        elif state_preparation == 'Coherent State':
            ops.Coherent(1) | q[0]
        
        ops.BSgate(pi/4, 0) | (q[0], q[1])
        
        ops.Rgate(phase1) | q[0]
        ops.Rgate(phase2) | q[1]
        
        ops.BSgate(pi/4, 0) | (q[0], q[1])
    
    eng = sf.Engine('fock', backend_options={"cutoff_dim": 5})
    result = eng.run(prog)
    
    state = result.state
    
    print()
    print("Simulation Results:")
    print("Most probable photon number for Mode 0:")
    probs = [state.fock_prob([n, 0]) for n in range(5)]
    print(f"{probs.index(max(probs))} photons")
    
    print("Most probable photon number for Mode 1:")
    probs = [state.fock_prob([0, n]) for n in range(5)]
    print(f"{probs.index(max(probs))} photons")

if __name__ == "__main__":
    main()
