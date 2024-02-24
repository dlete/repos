# Qiskit notebook

## 0 Oh!!... moments

How did we know that the amplitudes were 1/√2? Because they're the values that give us the right answers!

## 0 What is quantum?

‘Quantum physics’ is a term widely used but much less understood. It is a **mathematical model** first used to describe the **behavior of small things** in a laboratory, which exposed gaps in the preceding theory of ‘classical’ physics.

### The Quantum model

In short, quantum theory is probability theory with negative numbers.

What does this mean? We can’t have negative probabilities as that doesn’t make sense. To accommodate this, we use a new quantity we call amplitudes and plot these on trees instead. To get around the fact that we cannot have negative probabilities, and that all our probabilities must add up to 1, we use a mathematical trick: We square our amplitudes to calculate the probabilities.

|ψ⟩ = α|0⟩ + β|1⟩

Where α, β € C (are complex numbers)

α, β are 'amplitudes', probability amplitudes in fact.

The probability of encountering state |0⟩ is: P(|0⟩) = |⟨0|ψ⟩|^2

### Explaining the Double Quantum Coin Toss

Refer to the website, the explanation is very good thre. See here: <https://qiskit.org/textbook/what-is-quantum.html#Explaining-the-Double-Quantum-Coin-Toss>

## 1 Quantum States and Qubits

In quantum mechanics we call the column vectors kets and the row vectors bras. Together they make up bra-ket notation. Any ket |a⟩ has a corresponding bra ⟨a|, and we convert between them using the conjugate transpose.

In a circuit, we typically need to do three jobs:

1. First, encode the input,
2. then do some actual computation, and finally
3. extract an output.

In a quantum circuit:

* input is qubits
* output is bits

The extraction of outputs in a quantum circuit is done using an operation called ***measure***. Each measurement tells a specific qubit to give an output to a specific output bit. o, we can ask what does qubit 'x' output in bit 'y', where x = y or x ≠ y.

Qubits are always initialized to give the output 0.

The qubits and bits are both labelled by the numbers from 0 to n.
Qubits, you start counting from the top.
Bits, you start counting from the right (bit number and position in graph: 0 1 2 3 4 5; they are reversed really!!)

The reason for running many times and showing the result as a histogram is because quantum computers may have some randomness in their results.

Adding two circuits (e.g. qc_encode + qc_output) creates a new circuit

***half-adder***  
0+0 = 00 (in decimal, this is 0+0=0)  
0+1 = 01 (in decimal, this is 0+1=1)  
1+0 = 01 (in decimal, this is 1+0=1)  
1+1 = 10 (in decimal, this is 1+1=2)  

* Encoding an input

```bash
qc_encode = QuantumCircuit(n)
qc_encode.x(1)
qc_encode.x(5)

qc_encode.draw()
```

qc_ha.cx(0,2)
CNOT = XOR
do the operation Controlled NOT (CNOT) on quits 0 and 2, and put the result on qubit 2

### 1.3 Representing Qubit States

In quantum computers, our basic variable is the qubit: a quantum variant of the bit. These have exactly the same restrictions as normal bits do: they can store only a single binary piece of information, and can only ever give us an output of 0 or 1. However, they can also be manipulated in ways that can only be described by quantum mechanics. This gives us new gates to play with, allowing us to find new ways to design algorithms.

#### 1.3.1 Statevector

In classical physics we *describe* the position with a number number, say x = 4. That is deterministic.
In quantum physics, we use ***statevectors***, collection of numbers in a vector to *describe* the *state* of a system. Each element in the statevector contains the probability of finding the car in a certain place. That is probabilistic.

Classical physics. Describe the state **deterministically** with a vector.
Quantum physics. Describe the state **probabilistically** with a statevector.

#### 1.3.2 Qubit Notation

Whether we get a 0 or a 1 from a qubit only needs to be well-defined when a measurement is made to extract an output. At that point, it must commit to one of these two options. At all other times, its state will be something more complex than can be captured by a simple binary value.

***Qubit statevectors***

```math
|0⟩
|ψ⟩ = 1 |0⟩ + 0 |1⟩
|1|
|0|

|1⟩
|ψ⟩ = 0 |0⟩ + 1 |1⟩
|0|
|1|

|+⟩ 
|ψ⟩ = 1/√2 |0⟩ + 1/√2 |1⟩
|  1/√2 |
|  1/√2 |

|-⟩
|ψ⟩ = 1/√2 |0⟩ - 1/√2 |1⟩
|  1/√2 |
| -1/√2 |


|i⟩    |↻⟩
|ψ⟩ = 1/√2 |0⟩ + i 1/√2 |1⟩
|     1/√2 |
|   i 1/√2 |

|-i⟩   |↺⟩
|ψ⟩ = 1/√2 |0⟩ - i 1/√2 |1⟩
|     1/√2 |
| - i 1/√2 |
```

#### 1.3.2 The Rules of Measurement

##### 1.3.2.1 A Very Important Rule

There is a simple rule for measurement. To find the probability of measuring a state `|ψ⟩` in the state `|x⟩` we do:

`p(|x⟩)=|⟨x|ψ⟩|^2`

The symbols `⟨` and `|` tell us `⟨x|` is a row vector. In quantum mechanics we call the column vectors *kets* and the row vectors *bras*. Together they make up *bra-ket* notation.
Any ket `|a⟩` has a corresponding bra `⟨a|`, and we convert between them using the conjugate transpose.

The operation of `⟨x|ψ⟩` is the *inner product*. The result is a scalar.  
Could also do `|ψ⟩⟨x|` and in that case the operation is *outer product*. The result, a matrix of n x n, where n is the number of dimensions in `|ψ⟩` and `|x⟩`.

##### 1.3.2.2 The Implications of this Rule

* Normalisation  
The rule shows us that amplitudes are related to probabilities. If we want the probabilities to add up to 1 (which they should!), we need to ensure that the statevector is properly normalized. Specifically, we need the magnitude of the state vector to be 1.  
`⟨ψ|ψ⟩ = 1`

* Alternative measurement  
The measurement rule gives us the probability `p(|x⟩)` that a state `|ψ⟩` is measured as `|x⟩`. Nowhere does it tell us that `|x⟩` can only be either `|0⟩` or `|1⟩`. There is an infinite number of possible ways to measure a qubit. For any orthogonal pair of states, we can define a measurement that would cause a qubit to choose between the two.
(NOTE -> the **ortogonal** knob, the condition)

* Global Phase  
We know that measuring the state `|1⟩` will give us the output `1` with certainty. But we are also able to write down states such as

```math
|0|
|i| = i|1⟩
```

Here we find that the factor of i disappears once we take the magnitude of the complex number. This effect is completely independent of the measured state |x⟩. **It does not matter what measurement we are considering, the probabilities for the state `i|1⟩` are identical to those for `|1⟩`. Since measurements are the only way we can extract any information from a qubit, this implies that these two states are equivalent in all ways that are physically relevant**.

More generally, we refer to any overall factor `γ` on a state for which `|γ| = 1` as a 'global phase'. States that differ only by a global phase are physically indistinguishable.

`|⟨x|(γ|a⟩)|^2 = |γ⟨x|a⟩|^2 = |⟨x|a⟩|^2`

Note that this is distinct from the phase difference between terms in a superposition, which is known as the 'relative phase'. This becomes relevant once we consider different types of measurement and multiple qubits.

* The observer effect  
We know that the amplitudes contain information about the probability of us finding the qubit in a specific state, but once we have measured the qubit, we know with certainty what the state of the qubit is. For example, if we measure a qubit in the state:
`|ψ⟩ = α|0⟩ + β|1⟩`
And find it in the state `|0⟩`, if we measure again, there is a 100% chance of finding the qubit in the state `|0⟩`. This means the act of measuring changes the state of our qubits.

We sometimes refer to this as collapsing the state of the qubit. Measurements are therefore only used when we need to extract an output. This means that we often place all the measurements at the end of our quantum circuit.

##### A Note about Quantum Simulators

We can see that writing down a qubit’s state requires keeping track of two complex numbers, but when using a real quantum computer we will only ever receive a yes-or-no (0 or 1) answer for each qubit. The output of a quantum computer is bits, no superposition or complex amplitudes.

When using a real quantum computer, we cannot see the states of our qubits mid-computation, as this would destroy them! This behaviour is not ideal for learning, so Qiskit provides different quantum simulators: The `qasm_simulator` behaves as if you are interacting with a real quantum computer, and will not allow you to use `.get_statevector()`. Alternatively, `statevector_simulator`, does allow peeking at the quantum states before measurement.

#### 1.3.3 The Bloch Sphere

ϕ is/represents the the difference in phase between the states |0⟩ and |1⟩. The relative phase between them.

|0⟩
cartesians is [x=0, y=0, z=1]
spherical theta (θ) = 0, phi (ϕ) = 0

|1⟩
cartesians is [x=0, y=0, z=-1]
spherical theta (θ) = π, phi (ϕ) = 0

|+⟩
cartesians is [x=1, y=0, z=0]
spherical theta (θ) = π/2, phi (ϕ) = 0
statevector: 1/sqrt(2)(|0⟩ + |1⟩)

|-⟩
cartesians is [x=-1, y=0, z=0]
spherical theta (θ) = 3/2π, phi (ϕ) = 0
statevector: 1/sqrt(2)(|0⟩ - |1⟩)

|i⟩
in cartesians is [x=0, y=1, z=0]
in spherical theta (θ) = π/2, phi (ϕ) = π/2

|-i⟩
in cartesians is [x=0, y=-1, z=0]
in spherical theta (θ) = π/2, phi (ϕ) = 3/2 π

<http://qutip.org/>

#### 1.3.3.1 Describing the Restricted Qubit State

#### 1.3.3.2 Visually Representing a Qubit State

### 1.4 Single Qubit Gates

See the Gates section in this same file.

## 2. Multiple Qubits and Entanglement

`|ba⟩ = |b⟩ ⊗ |a⟩`

Representing multi-qubit states: as statevector of 2<sup>n</sup> dimensions, where `n` is the number of qubits.

|ψ⟩ = a<sub>00</sub>|00⟩ = a<sub>01</sub>|01⟩ + a<sub>10</sub>|10⟩ + a<sub>11</sub>|11⟩

How a single qubit gate acts on a qubit in a multi-qubit vector?. Answer: just as we used the tensor product to calculate multi-qubit statevectors, we use the tensor product to calculate matrices that act on these statevectors.

***Kickback*** is where the eigenvalue added by a gate to a qubit is ‘kicked back’ into a different qubit via a controlled operation. For example, we saw that performing an X-gate on a `|−⟩` qubit gives it the phase `−1`:  
`X|−⟩ = −|−⟩`

The interesting effect is when our control qubit is in superposition, the component of the control qubit that lies in the direction of |1⟩ applies this phase factor to the target qubit, which in turn kicks back a relative phase to our control qubit.

## To do

why is this? does that XOR happen automatically?
Use CNOTS to write both qubit 0 and 1 into qubit 2 -> that writing results in a XOR of the inputs on qubit 2

Investigate negative probabilities.

### negative amplitude probability in dobule measurement

Why is the amplitude tree of 1 /√2 for 0 and -1/√2 for 1 (note the minus - sign)?
And equally, why is the amplitude tree of 0 1/√2 for 0 and 1/√2 for 1 (note the plus + sign)?
Why one is positive and the other is negative?

See it clearly here: <https://qiskit.org/textbook/what-is-quantum.html#Explaining-the-Double-Quantum-Coin-Toss>

### H-gate, Hadamard, as outer product

Quick Exercise #1. Write the H-gate as the outer products of vectors |0⟩, |1⟩, |+⟩ and |−⟩.

### Hermitian

Since X is Hermitian, eigenvalues are real.
<https://quantumcomputing.stackexchange.com/questions/9577/how-to-find-eigenvalues-and-eigenvector-for-a-quantum-gate>

We call a complex matrix U as unitary if its conjugate transpose (Hermitian transpose) U† (or U∗) is its inverse i.e UU† = I.
<https://cse.iitkgp.ac.in/~goutam/quantumComputing/lect4part.pdf>

### global phase, understand, i do not think i do

You can re-run this cell a few times to reinitialise the qubit and measure it again. You will notice that either outcome is equally probable, but that the state of the qubit is never a superposition of |0⟩ and |1⟩. Somewhat interestingly, the global phase on the state |0⟩ survives, but since this is global phase, we can never measure it on a real quantum computer.

see "The observer effect" chapter 1, file 1.3 -> ...Somewhat interestingly, the global phase on the state |0⟩ survives, but since this is global phase, we can never measure it on a real quantum computer..... -> and the state of |0⟩ in the ψ⟩ is i|0⟩.

<https://quantumcomputing.stackexchange.com/questions/5125/what-is-the-difference-between-a-relative-phase-and-a-global-phase-in-particula>
<https://www.researchgate.net/post/Significance-of-the-Global-Phase-factor-in-Quantum-mechanics>

### is phase same than i?

see <https://arxiv.org/pdf/1903.04359.pdf>, see the gate Y: ...The effect of this gate is to flip a qubit’s |0⟩ and |1⟩ amplitudes and multiplies by an imaginary number (phase)...

### understand the effect of X|+⟩ and X|-⟩, Y|i⟩ and Y|-i⟩, Z|0⟩ and Z|1⟩

because X|-⟩ = 1/√2 (-|0⟩ + |1⟩)
, so, is
1/√2 (-|0⟩ + |1⟩)
the same than
1/√2 (|0⟩ + -|1⟩)

### is there relation between global phase and eigenvalues?

### unitary matrix

What is unitary matrix? sum of squared amplitudes is 1?
in 2.2 ...The unitary simulator multiplies all the gates in our circuit together to compile a single unitary matrix that performs the whole quantum circuit...

### outer product and visual `bra-ket`, e.g. |-+⟩ who multiplies who?

## References

backends, <https://medium.com/qiskit/qiskit-backends-what-they-are-and-how-to-work-with-them-fb66b3bd0463>

Feyman on negative provability, <https://cds.cern.ch/record/154856/files/pre-27827.pdf>

## Gates

An important feature of quantum circuits is that, between initialising the qubits and measuring them, the operations (gates) are always reversible!

These reversible gates can be represented as matrices, and as rotations around the Bloch sphere.

You may also notice that the Z-gate appears to have no effect on our qubit when it is in either of these two states |0⟩ or |1⟩. This is because the states |0⟩ and |1⟩ are the two eigenstates of the Z-gate.

### X

the X-gate switches the amplitudes of the states |0⟩ and |1⟩.

We can think of this gate as a rotation by π radians around the x-axis of the Bloch sphere. The X-gate is also often called a NOT-gate, referring to its classical analogue.

```math
X|0⟩ =    |1⟩
X|1⟩ =    |0⟩

X|+⟩ =  |+⟩
X|-⟩ = -|-⟩
```

### Y

We can think of this gate as a rotation by π radians around the y-axis of the Bloch sphere.

The effect of this gate is to flip a qubit’s |0⟩ and |1⟩ amplitudes and multiplies by an imaginary number (phase).

```math

Y|0⟩ =   i|1⟩
Y|1⟩ =  -i|0⟩

Y| i⟩ =  |i⟩
Y|-i⟩ = -|-i⟩
```

### Z

We can think of this gate as a rotation by π radians around the z-axis of the Bloch sphere.

```math
Z|0⟩ =    |0⟩
Z|1⟩ =   -|1⟩
```

### H, Hadamard

The Hadamard gate (H-gate) is a fundamental quantum gate. It allows us to move away from the poles of the Bloch sphere and create a superposition of |0⟩ and |1⟩.

This can be thought of as a rotation around the Bloch vector [1,0,1] (the line between the x & z-axis), or as transforming the state of the qubit between the X and Z bases.

```math
H|0⟩ = |+⟩
H|1⟩ = |−⟩

H|+⟩ = |0⟩  
H|-⟩ = |1⟩
```

### Rϕ

The Rϕ-gate is parametrised, that is, it needs a number (ϕ) to tell it exactly what to do. The Rϕ-gate performs a rotation of ϕ around the Z-axis direction (and as such is sometimes also known as the Rz-gate).

the Z-gate is a special case of the Rϕ-gate, with `ϕ = π`.

`.rz(<ϕ>, <qubit>)`

### Rx

### Ry

### I

The I-gate (aka ‘Id-gate’ or ‘Identity gate’). This is simply a gate that does nothing.

Applying the identity gate anywhere in your circuit should have no effect on the qubit state, so it’s interesting this is even considered a gate. There are two main reasons behind this, one is that it is often used in calculations, for example: proving the X-gate is its own inverse:

`I = XX`

The second, is that it is often useful when considering real hardware to specify a ‘do-nothing’ or ‘none’ operation.

### S

The next gate to mention is the S-gate (sometimes known as the √Z-gate), this is an Rϕ-gate with ϕ = π/2. It does a quarter-turn around the Bloch sphere. It is important to note that unlike every gate introduced in this chapter so far, the S-gate is not its own inverse! As a result, you will often see the S†-gate, (also “S-dagger”, “Sdg” or √Z†-gate). The S†-gate is clearly an Rϕ-gate with ϕ = −π/2

The name "√Z-gate" is due to the fact that two successively applied S-gates has the same effect as one Z-gate:
`SS|q⟩ = Z|q⟩`

```math
qc.s(0)   # Apply S-gate to qubit 0
qc.sdg(0) # Apply Sdg-gate to qubit 0
```

### T

The T-gate is an Rϕ-gate with ϕ = π/4. As with the S-gate, the T-gate is sometimes also known as the 4√Z-gate.

```math
qc.t(0)   # Apply T-gate to qubit 0
qc.tdg(0) # Apply Tdg-gate to qubit 0
```

### U, general U-gates

General U-gates

As we saw earlier, the I, Z, S & T-gates were all special cases of the more general Rϕ-gate. In the same way, the U3-gate is the most general of all single-qubit quantum gates. It is a parametrised gate of the form:

`U3(θ,ϕ,λ)` = see the matrix [here](https://qiskit.org/textbook/ch-states/single-qubit-gates.html#7.-General-U-gates--)

Every gate in this chapter could be specified as `U3(θ,ϕ,λ)`, but it is unusual to see this in a circuit diagram, possibly due to the difficulty in reading this.

Qiskit provides `U1` and `U2` gates, which are specific cases of the `U3`-gate in which `θ = ϕ = 0`, and `θ = π/2` respectively. You will notice that the `U1`-gate is equivalent to the `Rϕ-gate`.

`U3(π/2,ϕ,λ) = U2`  
`U3(0,0,λ) = U1`

Before running on real IBM quantum hardware, all single-qubit operations are compiled down to `U1` ,`U2` and `U3`. For this reason they are sometimes called the ***physical gates***.

### CNOT

A way of explaining the CNOT is to say that it does a NOT on the target if the control is 1, and does nothing otherwise.

This matrix swaps the amplitudes of |01⟩ and |11⟩ in our statevector

```math
      |a00|                 |a00|
|a⟩ = |a01|  then CNOT|a⟩ = |a11| <-
      |a10|                 |a10|
      |a11|                 |a01| <-
```

```math
CNOT|control target⟩
CNOT|0+⟩ = 1/√2 (|00⟩ + |11⟩)   # Bell state
CNOT|1+⟩ = 1/√2 (|01⟩ + |10⟩)
CNOT|++⟩ = |++⟩
CNOT|-+⟩ = |--⟩
CNOT|--⟩ = |+-⟩
CNOT|−0⟩ = |−⟩ ⊗ |0⟩ = |−0⟩
CNOT|−1⟩ = X|−⟩ ⊗ |1⟩ = −|−⟩ ⊗ |1⟩ = −|−1⟩
```

### Controlled-T

### Controlled-Z

The controlled-Z or cz gate is another well-used two-qubit gate. Just as the CNOT applies an X to its target qubit whenever its control is in state |1⟩ , the controlled-Z applies a Z in the same case. (if control is |1⟩, then apply z-gate to target?)

## Pearls

### Order of gates

If we write `U = XZH` that means that the H goes to qubit 0, Z goes to qubit 1, and X goes to qubit 2. Would look like
qc.

### add circuits

Adding the two circuits using qc_encode + qc_output creates a new circuit

### Simulators, `qasm_simulator` vs. `statevector_simulator`

The qasm_simulator behaves as if you are interacting with a real quantum computer, and will not allow you to use .get_statevector(). Alternatively, statevector_simulator, (which we have been using in this chapter) does allow peeking at the quantum states before measurement, as we have seen.

`unitary_simulator`, the unitary simulator multiplies all the gates in our circuit together to compile a single unitary matrix that performs the whole quantum circuit.

### Method: `.display()`

`display(plot_bloch_multivector(state))`
It is like the `print` of CLI but for pictures in Jupyter. It is like `qc.draw()`, but does put the picture inline and you can have more than one picture in the Jupyter cell.

### statevector formact for quiskit

a.+b.j, NOTE the ., with the . you are always safe

initial_state = [1.+0.j, 0.+0.j] # |ψ⟩ = |0⟩
in this also accepts
initial_state = [1, 0] # |ψ⟩ = |0⟩

### Symbols

|ψ⟩ = 1/√2
|ψ⟩ = α|0⟩ + β|1⟩
∈, epsilon
λ, lambda
θ, theta
ϕ, phi
π, pi
ψ, psy
psy, uppercase Ψ, lowercase ψ
γ
R
C
|↺⟩, |↻⟩, eigenstates of the Y-gate, equivalent of |i⟩ and |-i⟩
†, dagger
⊗, outer product, tensor product

Α α, alpha  
Β β, beta  
Γ γ, gamma  
Δ δ, delta  
Ε ε, epsilon  
Ζ ζ, zeta  
Η η, eta  
Θ θ, theta  
Ι ι, iota  
Κ κ, kappa  
Λ λ, lambda  
Μ μ, mu  
Ν ν, nu  
Ξ ξ, xi  
Ο ο, omicron  
Π π, pi  
Ρ ρ, rho  
Σ σ/ς, sigma  
Τ τ, tau  
Υ υ, upsilon  
Φ φ, phi  
Χ χ, chi  
Ψ ψ, psi  
Ω ω, omega
