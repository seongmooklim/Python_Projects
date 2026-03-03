## Title

### project 1

#### project 2



- $e^{ik\Delta x}+e^{−ik\Delta x}=2\cos(k\Delta x)$ /  $e^{ik\Delta x}-e^{−ik\Delta x}=2i\sin(k\Delta x)$ / $e^{ik\Delta x}+e^{ik\Delta x}-2 = -4\sin^2\frac{k \Delta x}{2}$ / $1−cos(k\Delta x)=2sin^2(\frac{k\Delta x}{2}​)$
- 푸아송 방정식 $\nabla^2 \phi = -\frac{\rho}{\epsilon_0}$의 이산화 형태는 $A \phi = -\frac{\rho}{\epsilon_0}$입니다. 따라서 $ρ=−ϵ_0​Aϕ$입니다.
- Crank-Nicolson (Semi / Full discretization)
	- Semi(Space): $\frac{\partial T}{\partial t} = \lambda\frac{\partial^2 T}{\partial x^2}, \lambda > 0 = \Rightarrow \frac{dT_i}{dt} = \lambda\frac{T_{i+1}-2T_i+T_{i-1}}{(\Delta x)^2}$
	- Full(Time/Space): $\frac{T_i^{n+1}-T_i^n}{\Delta t}=\frac{\lambda}{2}[\frac{T_{i+1}^{n+1}-2T_{i}^{n+1}+T_{i-1}^{n+1}}{(\Delta x)^2}-\frac{T_{i+1}^{n}-2T_{i}^{n}+T_{i-1}^{n}}{(\Delta x)^2}]$
- We consider the initial value problem $\frac{du}{dt} = Au$ with $u(t=0)=u_0$ with the tridiagonal matrix$$ A = \begin{pmatrix} 0&-1&0&1\\1&0&0&0\\0&0&0&-1\\0&0&1&0 \end{pmatrix}$$
	Find a suitable time integrator for this problem. Justify your choice and determine a bound for the time steps which ensures stability.
	- Analysis / 1. System Analysis: Matrix A is block-diagonal, representing two independent, identical 2D systems.
