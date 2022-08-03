import re

identifier = "_d_ddhimd1rk"

print(identifier == re.search("[a-zA-Z_]([0-9a-zA-Z_])*", identifier).group())
