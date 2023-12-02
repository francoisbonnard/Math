## concepts
- Perceptron Model to NN
- Activation functions
- Cost functions
- Feed Forward Netwroks
- BackPropagation

## Build our model abstractions

- Single Biological Neuron
- Perceptron
- multi layer perceptron model
- Deep Learning Neural Network (>2 hidden layers)

Zhou Lu & Boris Hanin proved that NN can approximate any [convex continuous function](https://mathworld.wolfram.com/ConvexFunction.html#:~:text=A%20convex%20function%20is%20a,the%20ends%20of%20the%20interval.)

[Universal Approximation Theorem](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_d%27approximation_universelle)

## [activation function](https://fr.wikipedia.org/wiki/Fonction_d%27activation)

- sigmoïde
- hyperbolic Tangent  
- Rectified Linear Unit (ReLU) -> useful for the issue of vanishing gradient

### Multi-class activation function

2 situations :
	- Non exclusive class	
	- Mutually Exclusive class ->	Softmax activated function / Calculates the probabilities distribution of the event over K different events (sum of all the probabilities = 1)

## Cost functions

also referred as loss function

y true value
z=w*x + b

neuron's prediction
$\sigma(z)=a $ 


quadratic cost function
$C = \frac{1}{2n}\sum_x ||y(x)  - a^L(x)||^2  $
$a^L$ activation output of the L layer (L=last layer)

Cost function is a function of 4 main components :
$C(W,B,S^r , E^r)$
$S^r$ : input of a single training sample
$E^r$ : desired output of that training sample 

## Gradient descent
minimize our loss/cost with w

Learning rate = step size

Adaptive gradient descent
Adam : a method for stochastic optimization

When dealing with N-dimensional vectors (tensors) the notation changes from derivative to gradient, this means we calculate :
∇C(W1,W2,...,Wn) (upside down triangle is the way to notate gradient)

For classification problems, we use the **Cross entropy** loss function. Assumption is that the model predicts a probability distribution p(y=i) for each class i=1,2,...,C

For a binary classification :
$-(ylog(p) + (1-y)log(1-p))$

For M number of classes >2
$-\sum_{c=1}^My_{0,c} log(P_{0,c}) $

## backpropagation

For the last layer :

$Z^L = w^La^{L-1} + b^L $
$ x = a^{L-1} $
$a^L = \sigma(Z^L) $
$C_0 (...) = (a^L - y)^2 $

reminder
$C = \frac{1}{2n}\sum_x ||y(x)  - a^L(x)||^2  $

We want to understand how sensitive is the cost function to change in w:
$\frac{\delta C_O}{\delta w^L} $ Partial derivative of the cost function with respect to weights

There is a chain rule :

$\frac{\delta C_O}{\delta w^L} = \frac{\delta z^L}{\delta w^L} \frac{\delta a^L}{\delta z^L} \frac{\delta C_O}{\delta a^L} $ 

And we can do the same for the bias :

$\frac{\delta C_O}{\delta b^L} = \frac{\delta z^L}{\delta b^L} \frac{\delta a^L}{\delta z^L} \frac{\delta C_O}{\delta a^L} $ 

Hadamard product

$\begin{bmatrix}
1 \\ 2 \end{bmatrix} ⨀ \begin{bmatrix} 3 \\ 4 \end{bmatrix}  = \begin{bmatrix} 1 & * & 3 \\ 2 & *& 4 \end{bmatrix} = \begin{bmatrix} 3 \\ 8 \end{bmatrix}$ 

## Step 3 : compute our error vector

$\delta^L = ∇_a C ⨀ \sigma^l (Z^L)   $

$∇_a C = (a^L -y) $ expressing the rate of change of C with respect to the output activations

y is the true value

## step 4 : backpropagate the error

for each layer L-1, L-2 ... we compute 

$\delta^l = (W^{l+1})^T \delta^{l+1} ⨀ \sigma^l (Z^l)   $
$ (W^{l+1})^T$ is the transpose of the weight matrix of $l+1$ layer

The gradient of the cost function is given by :

for each layer L-1, L-2 ... we compute 
$\frac{\delta C}{\delta w^l_{jk}}  = a^{l-1}_k \delta ^l_j $ 
$\frac{\delta C}{\delta b^l_{j}}  = \delta ^l_j $ 


https://mattmazur.com/2015/03/17/a-step-by-step-backpropagation-example/

## 39 pytorch gradients

    x = torch.tensor([[1.,2,3],[3,2,1]], requires_grad=True)
    y = 3*x + 2
    z = 2*y**2  
    out = z.mean()
    out.backward()
    print(x.grad)

tensor([[10., 16., 22.],
        [22., 16., 10.]])

You should see a 2x3 matrix. If we call the final <tt>out</tt> tensor "$o$", we can calculate the partial derivative of $o$ with respect to $x_i$ as follows:<br>

$o = \frac {1} {6}\sum_{i=1}^{6} z_i$<br>

$z_i = 2(y_i)^2 = 2(3x_i+2)^2$<br>

To solve the derivative of $z_i$ we use the <a href='https://en.wikipedia.org/wiki/Chain_rule'>chain rule</a>, where the derivative of $f(g(x)) = f'(g(x))g'(x)$<br>

In this case<br>

$f(g(x)) = 2(g(x))^2,\quad f'(g(x)) = 4g(x) \\
g(x) = 3x+2, \quad \quad g'(x) = 3 \\
\frac {dz} {dx} = 4g(x)\times 3  \quad = 12(3x+2) $

Therefore,<br>

$\frac{\partial o}{\partial x_i} = \frac{1}{6}\times 12(3x+2)$<br>

$\frac{\partial o}{\partial x_i}\bigr\rvert_{x_i=1} = 2(3(1)+2) = 10$

$\frac{\partial o}{\partial x_i}\bigr\rvert_{x_i=2} = 2(3(2)+2) = 16$

$\frac{\partial o}{\partial x_i}\bigr\rvert_{x_i=3} = 2(3(3)+2) = 22$