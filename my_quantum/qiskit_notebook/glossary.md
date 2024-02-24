# About

Glossary from Qiskit Notebook

## A

* ***amplitude***, in quantum mechanics, a probability amplitude is a complex number used in describing the behaviour of systems. The modulus squared of this quantity represents a probability density.

## B

* ***balanced, function***, returns 0's for exactly half of all inputs and 1's for the other half.
* ***barrier***, dashed lines in the image of a quantum circuit to distinguish the different parts of the circuit. Add with `circuit.barrier()`.
* ***binary string***, string of bits (classical) that represent information (a number, a character, a special character, etc.). See [ASCII, decimal, hexadecimal, octal, and binary conversion table](https://www.ibm.com/docs/en/aix/7.2?topic=adapters-ascii-decimal-hexadecimal-octal-binary-conversion-table)
* ***bra***, in quantum mechanics we call the column vectors kets and the row vectors bras.
* ***bra-ket***, notation for statevectors. Introduced by Dirac.

## C

* ***circuit diagram***, diagram showing inputs, operations (gates) and outputs.
* ***classical variables***, bits, objects made out of bits.
* ***classical computers***, computers that use classical variables.
* ***CNOT***, controlled-NOT, same that XOR in clasical. It is represented with the `cx(control, target)`command.
* ***collapsing***, when the state of a quantum state passes from being probabilisitic to deterministic, when passes from a quantum state to a classical state.
* ***constant, function***, returns all 0's or all 1's for any input
* ***`cx`***, see CNOT.
* ***`ccx`***, see Toffoli.

## D

* ***determinant***, `det(U)`, where `U` is a matrix

## E

* ***eigenstate***, one of the eigenvectors of M
* ***eigenvector of M***, vector v that when multipied by matrix M, is the same as doing a multiplication by a scalar: `M|v⟩ = λ|v⟩`
* ***eigenvalue***, the `λ` of an eigenvector of M.
* ***encode***, represent something in a given format/language.
* ***Euler's formula*** `e^(i pi) = -1`
* ***extraction***, see measure.

## G

* ***gate***, operation.

## H

* ***half-adder***, the collection of operations of adding two bits in all their possible combinations: 00, 01, 10, 11
* ***Hermitian matrix***, Hermitian matrix (or self-adjoint matrix) is a complex square matrix that is equal to its own conjugate transpose.

## I

* ***innitialize***, Qiskit method to transform the original state of a qubit into any state. Use with `circuit.initialize([α, β], <qubit>)`, where 'α' and 'β' are the probability amplitudes of `|0⟩` and `|1⟩`.
* ***inner product***, an inner product is a generalization of the dot product. In a vector space, it is a way to multiply vectors together, with the result of this multiplication being a scalar.

## K

* ***kets***, in quantum mechanics we call the column vectors kets
* ***kickback***, see phase kickback

## L

* ***linearly independent*** vectors, means we cannot describe one in terms of the other.

## M

* ***matrix, hermitian***, when U<sup>†</sup> = U, where U<sup>†</sup> is the conjugate transpose

* ***matrix, unitary***, when U<sup>†</sup> = U<sup>-1</sup> where the inverse U<sup>-1</sup> is such that A × A-1 = A-1 × A = I

* ***measure***, the extraction of outputs in a quantum circuit is done using an operation called measure.

## N

* ***norm***
* ***NOT***, Boolean gate that flips the value of the bit. It flips the bit value: 0 becomes 1 and 1 becomes 0. For qubits, it is an operation called `x(qubit)` that does the job of the NOT.

## O

* ***orthonormal*** base. Ortho = perpedicular; Normal = 1. Orthogonal and normalised. Orthogonal means the vectors are at right angles. And normalised means their magnitudes (length of the arrow) is equal to 1.

* ***outer product***, n linear algebra, the outer product of two coordinate vectors is a matrix. If the two vectors have dimensions n and m, then their outer product is an n × m matrix. More generally, given two tensors (multidimensional arrays of numbers), their outer product is a tensor. The outer product of tensors is also referred to as their tensor product.

## P

* ***phase kickback*** is where the eigenvalue added by a gate to a qubit is ‘kicked back’ into a different qubit via a controlled operation. For example, we saw that performing an X-gate on a `|−⟩` qubit gives it the phase `−1`:  
`X|−⟩ = −|−⟩`

* ***physical gates***, the gates `U1` ,`U2` and `U3`. Before running on real IBM quantum hardware, all single-qubit operations are compiled down to `U1` ,`U2` and `U3`. For this reason they are sometimes called the ***physical gates***.

* ***probability tree***, drawing to map out every possible eventuality and from this, we can calculate the chance of it happening.

* ***`ψ`, psi***

## Q

* ***quantum circuit***, a quantum circuit is a computational routine consisting of coherent quantum operations on quantum data, such as qubits, and concurrent real-time classical computation. It is an ordered sequence of quantum gates, measurements and resets, all of which may be conditioned on and use data from the real-time classical computation.

* ***qubit***, basic variable in quantum computers. The quantum variable of the bit. Before measuring the qubit, it can be in any state and at the same time. After measuring can only be in the states 0 or 1; and stays there, it has collapsed.
* ***qubit statevector***, description of a qubit state in the form of a statector, e.g.: `|ψ⟩ = α|0⟩ + β|1⟩`

## S

* ***statevectors***, in quantum physics, collection of numbers in a vector to describe the state of a system.
* ***superposition***, in quantum mechanics, we typically describe linear combinations such as this using the word *'superposition'*. Statevector is not entirely `|0⟩` and not entirely `|1⟩`, instead, it is described by a linear combination of the two.

## T

* ***tensors*** multidimensional arrays of numbers.
* ***tensor product***, same than outer product. See outer product.
* ***Toffoli***, (two controls and one target) performs a NOT on the target qubit only when both controls are in state 1. It is like an AND in Boolean gates. It is represented with the `ccx(control, control, target)` command.

* ***tree***, see probability tree.

## X

* ***x***, see NOT.
* ***XOR***, Boolean gate on two input bits that outputs 0 when both inputs are the same and 1 when different. See CNOT.
