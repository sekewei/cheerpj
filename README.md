# CheerpJ Java Stack Demo

A small HTML and Java demonstration that runs a Java stack class in the browser using [CheerpJ](https://leaningtech.com/cheerpj/).

The Java class `MyStack` uses `ArrayDeque` to implement `push`, `pop`, `peek`, `contents`, and `export`. The HTML page calls these Java methods through CheerpJ and displays the returned stack values.

[Demo@github.io](https://sekewei.github.io/cheerpj/cheerpj.html)

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

Then open:

<http://localhost:8001/cheerpj.html>

`run.sh` builds `MyStack.jar` and starts the range-enabled Python server. CheerpJ needs this server to load JAR files correctly.

To use another port:

```bash
./run.sh 8080
```

Open <http://localhost:8080/cheerpj.html>.

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

1. Enter a value.
2. Select **Push** to add it to the Java stack.
3. Select **Peek** to view the top value.
4. Select **Pop** to remove the top value.
5. Select **Export** to retrieve and display all stack elements.

The first pushed value appears at the bottom. Later values are placed above it, matching LIFO behavior.

## Project files

| File | Purpose |
| --- | --- |
| `cheerpj.html` | Browser interface and CheerpJ Java calls |
| `MyStack.java` | Java stack implementation using `ArrayDeque` |
| `MyStack.jar` | Compiled Java class loaded by CheerpJ |
| `build.sh` | Compiles `MyStack.java` and creates the JAR |
| `run.sh` | Builds the project and starts the local server |
| `server.py` | Python HTTP server with byte-range support |

## Add or update a Java class

### Replace `MyStack.java`

Edit the Java source, then rebuild the JAR:

```bash
./build.sh
```

Refresh the browser with **Command+R**. If the browser uses an old JAR, use a hard refresh or update the query version in `cheerpj.html`:

```javascript
const stackJar = "/MyStack.jar?v=11";
```

### Add a separate Java class

Suppose the new class is named `Calculator`.

1. Create `Calculator.java` in this directory.
2. Compile it:

   ```bash
   javac Calculator.java
   ```

3. Create its JAR:

   ```bash
   jar cfe Calculator.jar Calculator Calculator.class
   ```

4. Update the HTML class and JAR paths:

   ```javascript
   const calculatorJar = "/Calculator.jar?v=1";
   await cheerpjInit({ preloadResources: [calculatorJar] });
   await cheerpjRunMain("Calculator", "/app/Calculator.jar");
   const calculator = await cjNew("Calculator");
   ```

5. Call public Java methods with `cjCall`:

   ```javascript
   const result = await cjCall(calculator, "add", 2, 3);
   ```

6. Update `build.sh` if the new class should be built automatically:

   ```sh
   javac MyStack.java Calculator.java
   jar cfe MyStack.jar MyStack MyStack.class
   jar cfe Calculator.jar Calculator Calculator.class
   ```

### Add a Java class with dependencies

If a class uses multiple source files, compile all of them and include the resulting class files in the JAR:

```bash
javac Calculator.java CalculatorUtils.java
jar cfe Calculator.jar Calculator Calculator.class CalculatorUtils.class
```

For larger projects, use a Java build tool such as Maven or Gradle instead of maintaining JAR commands manually.

## Important CheerpJ paths

The browser uses two related paths:

- `/MyStack.jar` is the URL requested by the browser.
- `/app/MyStack.jar` is the CheerpJ class path used by `cheerpjRunMain`.

Keep the JAR filename consistent in both places. The server runs from this project directory, so the JAR must be stored beside `cheerpj.html`.

## Troubleshooting

### `javac: command not found`

Install a JDK, not only a Java runtime. Confirm that `javac -version` works, then run:

```bash
./build.sh
```

### `CheerpJ: Already initialized`

Reload the page. The HTML stores the initialization promise and should initialize CheerpJ only once per page load.

### Java changes do not appear

Rebuild the JAR and refresh the browser. Increment the `?v=` value in `cheerpj.html` to bypass browser caching.

### The JAR cannot be loaded

Start the project server with `./run.sh`. Do not open `cheerpj.html` directly with a `file://` URL, and do not use a basic server that lacks byte-range support.
