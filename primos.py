PS C:\Users\UENDEL> cd C:\Users\UENDEL
>> python primos.py
  File "C:\Users\UENDEL\primos.py", line 5
    return True
    ^^^^^^
IndentationError: expected an indented block after 'if' statement on line 4
PS C:\Users\UENDEL> py primos.py
  File "C:\Users\UENDEL\primos.py", line 5
    ^^^^^^
IndentationError: expected an indented block after 'if' statement on line 4
PS C:\Users\UENDEL> py cd $env: userprofile/downloads
No linha:1 caractere:7
+ py cd $env: userprofile/downloads
+       ~~~~~
Referência de variável inválida. ':' não era seguido de um caractere de nome de variável válido. Considere usar ${}     
para delimitar o nome.
 
PS C:\Users\UENDEL> ]C:\Users\UENDEL\Downloads\
] : O termo ']' não é reconhecido como nome de cmdlet, função, arquivo de script ou programa operável. Verifique a      
grafia do nome ou, se um caminho tiver sido incluído, veja se o caminho está correto e tente novamente.
No linha:1 caractere:1
+ ]C:\Users\UENDEL\Downloads\
+ ~
    + CategoryInfo          : ObjectNotFound: (]:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
 
PS C:\Users\UENDEL>
PS C:\Users\UENDEL> + py cd $env: userprofile/downloads
No linha:1 caractere:2
+ + py cd $env: userprofile/downloads
+  ~
Expressão ausente após operador unário '+'.
+ + py cd $env: userprofile/downloads
+   ~~
Token 'py' inesperado na expressão ou instrução.
No linha:1 caractere:9
+ + py cd $env: userprofile/downloads
+         ~~~~~
Referência de variável inválida. ':' não era seguido de um caractere de nome de variável válido. Considere usar ${}     
para delimitar o nome.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : MissingExpressionAfterOperator
 
PS C:\Users\UENDEL> + py cd $env: userprofile/downloads
No linha:1 caractere:2
+ + py cd $env: userprofile/downloads
+  ~
Expressão ausente após operador unário '+'.
+ + py cd $env: userprofile/downloads
+   ~~
Token 'py' inesperado na expressão ou instrução.
No linha:1 caractere:9
+ + py cd $env: userprofile/downloads
+         ~~~~~
Referência de variável inválida. ':' não era seguido de um caractere de nome de variável válido. Considere usar ${}     
para delimitar o nome.
    + FullyQualifiedErrorId : MissingExpressionAfterOperator

PS C:\Users\UENDEL> cd $env: userprofile/downloads
No linha:1 caractere:4
+ cd $env: userprofile/downloads
+    ~~~~~
Referência de variável inválida. ':' não era seguido de um caractere de nome de variável válido. Considere usar ${}     
para delimitar o nome.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : InvalidVariableReferenceWithDrive

PS C:\Users\UENDEL> py primos.py
[2, 3, 5, 7, 11, 13, 17, 19, 23]
PS C:\Users\UENDEL>