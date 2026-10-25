# Surya figure count vs label drawings

For every page the label says how many drawings there are; Surya's tags (data/tags/) say how
many figure/table regions it found. Per split and source: exact-count accuracy, and count-level
precision / recall (matched = min of the two counts per page). Before the renderer's merging of
over-split boxes, so this measures Surya itself.

| split | source | pages | label drawings | Surya regions | exact count | precision | recall |
|---|---|---|---|---|---|---|---|
| train | hlcs | 15 | 10 | 11 | 0.933 | 0.909 | 1.000 |
| train | ie643 | 151 | 102 | 135 | 0.775 | 0.681 | 0.902 |
| train | ie802 | 40 | 47 | 59 | 0.550 | 0.712 | 0.894 |
| train | mlt | 97 | 47 | 66 | 0.835 | 0.712 | 1.000 |
| train | ALL | 303 | 206 | 271 | 0.772 | 0.705 | 0.927 |
| val | hlcs | 1 | 0 | 0 | 1.000 | - | - |
| val | ie643 | 20 | 8 | 8 | 1.000 | 1.000 | 1.000 |
| val | ie802 | 4 | 10 | 13 | 0.250 | 0.769 | 1.000 |
| val | mlt | 6 | 0 | 4 | 0.500 | 0.000 | - |
| val | ALL | 31 | 18 | 25 | 0.806 | 0.720 | 1.000 |
| test | hlcs | 4 | 0 | 0 | 1.000 | - | - |
| test | ie643 | 34 | 11 | 11 | 0.794 | 0.636 | 0.636 |
| test | ie802 | 12 | 14 | 15 | 0.917 | 0.933 | 1.000 |
| test | mlt | 26 | 25 | 26 | 0.962 | 0.962 | 1.000 |
| test | ALL | 76 | 50 | 52 | 0.882 | 0.885 | 0.920 |
| all | ALL | 410 | 274 | 348 | 0.795 | 0.733 | 0.931 |
