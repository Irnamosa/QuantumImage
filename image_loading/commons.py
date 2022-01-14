from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute
from qiskit import IBMQ, Aer
from qiskit.circuit import Parameter
from qiskit.quantum_info import partial_trace, DensityMatrix
try:
    from qiskit.providers.ibmq import RunnerResult
except:
    None

def runReal(QCs, backend='ibmq_montreal', opt=0):
    '''
    Run QCs on backend 
    '''
    option = {'backend_name': backend}
    
    runtime_inputs_copy = runtime_inputs.copy() 
    runtime_inputs_copy['circuits'] = QCs
    runtime_inputs_copy['optimization_level'] = opt
    
    job = provider.runtime.run(
                program_id='circuit-runner',
                options=option,
                inputs=runtime_inputs_copy)
    
    print(job.job_id())
    
    return job

def getCounts(jobs):
    return job.result(decoder=RunnerResult).get_counts()

provider = IBMQ.get_provider(
    hub='ibm-q-melbourne',
    group='internal',
    project='default'
)

runtime_inputs = {
  # A circuit or a list
  # of circuits.
  'circuits': None, # A QuantumCircuit or a list of QuantumCircuits. (required)
    
  # Number of repetitions of each
  # circuit, for sampling. Default: 1024.
  'shots': 8192, # int
    
  # Initial position of virtual qubits
  # on physical qubits.
  'initial_layout': None, # dict or list
    
  # Name of layout selection pass
  # ('trivial', 'dense', 'noise_adaptive', 'sabre')
  'layout_method': None, # string
    
  # Name of routing pass ('basic',
  # 'lookahead', 'stochastic', 'sabre').
  'routing_method': None, # string
    
  # Name of translation pass ('unroller',
  # 'translator', 'synthesis').
  'translation_method': None, # string
    
  # Sets random seed for the
  # stochastic parts of the transpiler.
  'seed_transpiler': None, # int
  
  # How much optimization to perform
  # on the circuits (0-3). Higher
  # levels generate more optimized circuits.
  # Default is 1.
  'optimization_level': 0, # int
  
  # Whether to reset the qubits
  # to the ground state for
  # each shot.
  'init_qubits': True, # bool
  
  # Delay between programs in seconds.
  'rep_delay': None, # float
  
  # Additional compilation options.
  'transpiler_options': None, # dict
  
  # Whether to apply measurement error
  # mitigation. Default is False.
  'measurement_error_mitigation': True # bool
}