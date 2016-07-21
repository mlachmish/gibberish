# gibberish
gibberish is a tool for iOS developer that help test your application UI befor sending it to translation.
<br><br>
gibberish will generate '.strings' file with long gibberish strings from an existing '.strings' file while saving each string format.

## How to install
```bash
$ brew install gibberish
```

## How to use
```bash
$ gibberish <path to existing '.strings'> <path to gibberish '.strings'>
```

gibberish will generate <b>a new</b> '.strings' file that will have all the original keys but with gibberish values with the same format.<br><br>
For example:<br>
<u>original</u>
```bash
"welcome.prompt" = "Welcome %@, have a good day!"
```
<br>

<u>gibberish</u>
```bash
"welcome.prompt" = "jy6Ks8Ew%smSi7H2Sc@ %@, 887sSAD03sdaSD asdSAD sad<MNSAKFLJf!"
```
<br>
Now you need to build your app with the new '.strings' file and see what broke in your UI.

## Author

Matan Lachmish <sub>a.k.a</sub> <b>The Big Fat Ninja</b> <img src="assets/TheBigFatNinja.png?raw=true" alt="The Big Fat Ninja" width="13"><br>
https://thebigfatninja.xyz

## License

gibberish is available under the MIT license. See the LICENSE file for more info.
