Gradient computation in a programmatic way.

```
opt.zero_grad()
loss.backward()
opt.update_step()
```

**Automatic differentiation:**

```
Class MLP:
  ...
  def forward(x):
```

[Diagram: input layer box → hidden layer box → output layer box, chained left to right.]
