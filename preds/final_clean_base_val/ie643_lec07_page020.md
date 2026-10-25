```markdown
# Lecture Notes on Quantum Mechanics

## Introduction

Quantum mechanics is a fundamental theory in physics that describes the physical properties of nature at the scale of atoms and subatomic particles.

## Key Concepts

### Wave Functions

A wave function $\psi(x)$ represents the state of a quantum system. It satisfies the Schrödinger equation:

$$
i\hbar \frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2m}\nabla^2\psi + V\psi
$$

where $\hbar$ is the reduced Planck constant, $m$ is the mass of the particle, and $V$ is the potential energy.

### Probability Amplitude

The probability amplitude $\psi(x)$ can be complex-valued. The probability density is given by:

$$
|\psi(x)|^2
$$

which gives the likelihood of finding the particle at position $x$.

### Superposition Principle

Particles can exist in multiple states simultaneously until observed. This principle is described by the superposition of wave functions:

$$
\psi(x) = \sum_{i} c_i \psi_i(x)
$$

where $c_i$ are complex coefficients representing the probability amplitudes.

### Measurement and Collapse

When a measurement is made, the wave function collapses to one of the eigenstates with probabilities proportional to the squared magnitudes of the corresponding coefficients.

## Examples

1. **Harmonic Oscillator**

   The harmonic oscillator is a simple model where a particle moves in a potential well defined by a spring force. The wave function for the nth excited state is:

   $$\psi_n(x) = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4} e^{-m\omega x^2/2\hbar} H_n\left(\sqrt{m\omega/\hbar}x\right)$$

   where $H_n$ are Hermite polynomials.

2. **Schrödinger Equation**

   The time-independent Schrödinger equation for a particle in a potential $V(x)$ is:

   $$-\frac{\hbar^2}{2m}\nabla^2\psi + V\psi = E\psi$$

   where $E$ is the energy of the particle.

## Conclusion

Understanding quantum mechanics requires a deep dive into the mathematics and principles behind wave functions, superposition, and measurement. These concepts form the basis for much of modern physics and technology.
```