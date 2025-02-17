"""
One of the encoder circuits from:https://arxiv.org/abs/1612.02806
"""
import pennylane as qml


def e1_classic(params, wires):
    """
    :params: an array of gate parameters of len. nr_params
    :wires: list of qubits on which decoder is applied
    nr_params = 2*3*len(wires)+ 3*(len(wires)-1)*len(wires)
    """

    # Add the first rotational gates:
    idx = 0
    for i in wires:
        # qml.Rot(phi, theta, omega, wire)
        qml.Rot(params[idx], params[idx + 1], params[idx + 2], wires=i)
        idx += 3

    # Add the controlled rotational gates
    for i in wires:
        for j in wires:
            if i != j:
                qml.CRot(params[idx], params[idx + 1], params[idx + 2], wires=[i, j])
                idx += 3

    # Add the last rotational gates:
    for i in wires:
        # qml.Rot(phi, theta, omega, wire)
        qml.Rot(params[idx], params[idx + 1], params[idx + 2], wires=i)
        idx += 3


def e2_classic(params, wires):
    """
    :params: an array of gate parameters of len. nr_params
    :wires: list of qubits on which decoder is applied
    nr_params = 15 * len(wires)*(len(wires)-1)/2
    """
    idx = 0

    for j in range(1, len(wires)):
        i = 0
        while i + j < len(wires):
            # qml.Rot(phi, theta, omega, wire)
            qml.Rot(params[idx], params[idx + 1], params[idx + 2], wires=i)
            qml.Rot(params[idx + 3], params[idx + 4], params[idx + 5], wires=i + j)
            qml.CNOT(wires=[i + j, i])
            qml.RZ(params[idx + 6], wires=i)
            qml.RY(params[idx + 7], wires=[i + j])
            qml.CNOT(wires=[i, i + j])
            qml.RY(params[idx + 8], wires=[i + j])
            qml.CNOT(wires=[i + j, i])
            qml.Rot(params[idx + 9], params[idx + 10], params[idx + 11], wires=i)
            qml.Rot(params[idx + 12], params[idx + 13], params[idx + 14], wires=i + j)

            i += 1
            idx += 15
