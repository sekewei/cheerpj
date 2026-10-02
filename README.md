# CheerpJ 3 Java Stack Demo

A small HTML and Java demonstration of running Java in the browser with [CheerpJ 3](https://leaningtech.com/cheerpj/). The page loads the compiled `MyStack3.class` file directly from the web-server root and calls its methods through CheerpJ library mode.

`MyStack3.class` is compiled for Java 8, which is the bytecode version supported by the CheerpJ 3.0 runtime used by this demo.

[Live demo](https://sekewei.github.io/cheerpj/cheerpj-v3.html)

## Requirements

- macOS, Linux, or Windows
- Java Development Kit (JDK), including `javac` and `jar`
- Python 3
- A modern browser

Check the tools:

```bash
java -version
javac -version
python3 --version
```

## Install a JDK on macOS

Using Homebrew:

```bash
brew install openjdk
```

If the commands are not found after installation, follow Homebrew's suggested `PATH` instructions and restart Terminal.

## Build and run

From the project directory:

```bash
cd github/cheerpj
./run.sh
```

`run.sh` builds `MyStack3.class` for Java 8 and starts the local Python server, which supports HTTP byte-range requests. Open the demo at:

<http://localhost:8001/cheerpj-v3.html>

To use another port:

```bash
./run.sh 8080
```

Open <http://localhost:8080/cheerpj-v3.html>.

To build without starting the server:

```bash
./build.sh
```

Stop the server with **Control+C**.

## Upload to GitHub

Create an empty repository on GitHub, then run these commands from this directory. Replace `YOUR_USERNAME` and `YOUR_REPOSITORY` with your GitHub values.

```bash
cd github/cheerpj
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
```

For later changes:

```bash
git add .
git commit -m "Describe the change"
git push
```

Check the configured remote with:

```bash
git remote -v
```

## Use the demo

Select **Push**, **Peek**, or **Pop**. Each result is prepended to the output, with earlier messages retained below it.

## Project files

| File | Purpose |
| --- | --- |
| `cheerpj-v3.html` | CheerpJ 3 browser interface loading a class from `/app/` |
| `MyStack3.java` | Java stack implementation |
| `MyStack3.class` | Java 8 class file built for the demo |
| `build.sh` | Compiles `MyStack3.java` for Java 8 |
| `run.sh` | Builds the class file and starts the local server |
| `server.py` | Python HTTP server with byte-range support |

## Add or update a Java class

The demo serves `MyStack3.class` from the project root. Its classpath is `/app/`, which maps to that web-server root. No JAR is needed.

`build.sh` compiles the class with `javac --release 8`. To load another default-package class from the same directory, resolve it from the library object and instantiate it:

```javascript
await cheerpjInit();
const lib = await cheerpjRunLibrary("/app/");
const Calculator = await lib.Calculator;
const calculator = await new Calculator();
```

Call Java methods directly on the instance and await their results. For classes in packages, preserve the package directory structure under the web root and resolve the class through its package path, such as `lib.com.example.Calculator`.

For classes with dependencies, compile all source files for Java 8 and make the resulting `.class` files available under the web root:

```bash
javac --release 8 Calculator.java CalculatorUtils.java
```

## Important CheerpJ paths

`cheerpjRunLibrary("/app/")` loads the project directory as the classpath. The `/app/` virtual path maps to the web-server root, where `MyStack3.class` is served directly.

## Troubleshooting

### `javac: command not found`

Install a JDK, not only a Java runtime. Confirm that `javac -version` works, then run:

```bash
./build.sh
```

### `CheerpJ: Already initialized`

Reload the page. The HTML stores the initialization promise and should initialize CheerpJ only once per page load.

### Java changes do not appear

Run `./build.sh` to rebuild `MyStack3.class`, then refresh the page.

### Java files cannot be loaded locally

Start the project server with `./run.sh`; it supports byte-range requests used by CheerpJ. Do not open the HTML directly with a `file://` URL. GitHub Pages also supports byte ranges, so the custom Python server is only needed for local development.
