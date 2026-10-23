# Multi-task Learning

[Diagram: A diagram illustrating object detection on an image. Two bounding boxes are drawn: one around a "cat" region at the top right and another around a "dog" region at the bottom left. Arrows indicate two tasks: Task 1 (classification into labels like "cat" and "dog") and Task 2 (regression for bounding box region specification).]

## Task 1
- Object classification / labeling: `cat`, `dog`

## Task 2 (Regression)
- **Region specification**: $(\text{top}, \text{left}, \text{bottom}, \text{right})$
  - Example coordinates: $4.6$, $0.8$, $29.3$, $0.5$