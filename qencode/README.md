
## QENCODE

This module is part of the [QuanutmAutoEncoders](https://github.com/stephendiadamo/QuantumAutoEncoders/blob/main/qencode/qubits_arrangement.py) repository. 
This module aims to keep all the pieces of an autoencoder easy to connect with each other by using QubitsArrangement class.
It also provides a range of: initializers, encoder, and decoder circuits that we implemented using [Pennylane](https://pennylane.ai/).

Code structure:
------------

    │
    ├── decoders                                               
    │   ├── base.py                                        <- basic decoder
    │   ├── classic_parametrized_decoder.py        	       <- an example of a parametrized decoder
    │   └── ent_assist_decoder.py                          <- entanglement assisted decoder    
    │
    ├── encoders 
    │   ├── base.py                                         <- encoder circuits from:https://arxiv.org/abs/1612.02806
    │   ├── enhance_e3.py                                   <- encoder circuit inspired  from the: https://arxiv.org/abs/2010.06599      
    │   └── ent_assist_ecoder.py                            <- entanglement assisted encoder with no interaction 
    │
    ├── initialize                       			
    │   └── base.py                                	         <- colection of pennylane initializers addapted to our project 
    │
    ├── training_circuits ( a coection of helpful quantum circuits)                                                
    │   └── swap_test.py                                    <- Swap test circuit      
    │
    ├── utils (utility function for implementing examples) 
    │   └── mnist.py 					                    <- function to import nmist data set
    │   
    ├── qubits_arrangement.py                       	    <- we use this class to keep our qubit register in order
    │   
    ├── requirements.txt                                    <-  requirements for qencode module
    │
    └──README.md                                            <- qencode README .
    


--------
