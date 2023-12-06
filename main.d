int a = 2; # int declaration example
double b = 3.5;
bool isD = True;
string fileExtension = ".d";

print(b);
print(fileExtension);

func isGreater(int a, int b) -> bool {
  return a > b;
}

func showMessage(string message) -> void {
  print(message);
}

while (isD == True) {
  a = a * 2;
  print(a);

  if (a > 1000) {
    isD = False;
  }
}
