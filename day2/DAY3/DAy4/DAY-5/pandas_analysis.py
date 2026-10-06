import pandas as pd
data = {
"name":["Alice", "Bob", "Carol", "David", "Eve" ],
"score":[88 , 42 , 67 , 35 , 91]
}
df = pd.DataFrame(data)
top_score = df["score"].max()
print(f"Top Score is : {top_score}")
df["passed"] = df["score"]>=50
num_passed = df["passed"].sum()
print(f"Passed:{num_passed}")