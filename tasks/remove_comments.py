code = """// program to print a text

#include <iostream>
using namespace std;

// display a number
/*void displayNum(int n1, float n2) {
    cout << "The int number is " << n1;
    cout << "The double number is " << n2*/;
}

int main() {
     
     int num1 = 5;
     double num2 = 5.5;

    // calling the function
    displayNum(num1, num2);

    return 0;
}"""

def remove_comments(code):
  default = 0
  single_comment = 1
  multi_comment = 2
  string = 3
  mode = default
  pos = 0
  max_pos = len(code) - 1
  while pos <= max_pos:
    sym = code[pos]
    if mode == default:
      if sym == '/':
        candidate_sym = code[pos:min(pos+2, max_pos+1)]
        if candidate_sym in ['//', '/*']:
          pos += 1
          sym = candidate_sym
      if sym == '//':
        mode = single_comment
      elif sym == '/*':
        mode = multi_comment
      else:
        if sym == '\"':
          mode = string
        yield sym
    elif mode == string:
      if sym == '\"':
        mode = default
      yield sym
    elif mode == single_comment:
      if sym == '\n':
        mode = default
        yield sym
    else: # mode == multi_comment
      if sym == '*' and code[pos:min(pos+2, max_pos+1)] == '*/':
        pos += 1
        mode = default
    pos += 1

print(''.join([c for c in remove_comments(code)]))
