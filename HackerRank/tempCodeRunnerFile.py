str = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
wi = 4 
ans = ""
for i in range(0,len(str),wi):
    ans.join(str[i:i+wi])
    ans.join("\n")
print(ans)