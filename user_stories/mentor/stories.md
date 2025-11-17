## User Stories

### P0: Random Fun Fact Generator
As an engineer, I want to be able to get a random fun fact from a database, so that I can share them with my team.

---

## Implementation Details

### HTTP Handler (REST)
The handler bridges the database layer and the UI layer, allowing the random fact generator page to display facts and fetch new ones without page refreshes. Prior to the implementation of HTML, this will just be a JSON response.

#### Steps:
1. Implement the `get_route()` method in `get_fact.py`.

```python
def get_route():
    fact = get_fact()
    wants_json = request.args.get("json") in ("1", "true", "True")
    if wants_json:
        return jsonify({
            "id": getattr(fact, "id", None),
            "fact": fact.fact,
        })
    return render_template("generate.html",
                         random_fact=fact.fact,
                         random_fact_id=fact.id,
    )
```

---

### Database Layer
The database implementation fetches a single random fact from the PostgreSQL database.

#### Steps:
1. Implement the `get_fact()` method in `get_fact.py`.

```python
def get_fact() -> Fact:
    provider = PostgresConnectionProvider()
    with provider.cursor() as cur:
        cur.execute("SELECT id, fact FROM facts ORDER BY RANDOM() LIMIT 1;")
        result = cur.fetchone()
        if result:
            return Fact(id=result[0], fact=result[1])
        else:
            return Fact(id=None, fact="No facts found.")
```

---

### REST Router
#### Steps:
1. Add a `generate` route with a `GET` method to `router.py`.
2. Visit `/generate` on localhost to see a fact.

```python
from flask import Flask
from .home import home_route
from .get_fact import get_route

def create_app():
    app = Flask(__name__,
                template_folder='../templates',
                static_folder='../static')
    app.add_url_rule("/", view_func=home_route, methods=["GET"])
    app.add_url_rule("/generate", view_func=get_route, methods=["GET"])

    # Print all registered routes
    print("Registered routes:")
    for rule in app.url_map.iter_rules():
        print(f"{rule} -> {rule.methods}")
    return app
```

```
{
    "fact": "Honey never spoils."
}
```
---

### Unit Tests
1. Add unit tests to cover the generate fact logic.
2. Place tests in the same directory as the original file, following the convention `filename_test.py`.
3. Reference the given happy path & unit test guide located in the same folder and encourage students to think about negative cases to improve test coverage.

---

### HTML Integration
1. Add HTML to present the fact nicely.

In `templates/generate.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Random Fact Generator</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
</head>
<body>
    <div class="page-container generate-container">
        <!-- Navbar -->
        {% include './partials/navbar.html' %}

        <div class="main-container">
            <h1>Random Fact Generator</h1>
            <div class="fact-container">
                <p>Your random fact is: </p>
                <strong id="fact-text">{{ random_fact }}</strong>
            </div>
            <button class="fact-generator-button" onclick="getNewFact()">
            <span id="button-text">New Fact</span>
            </button>
        </div>

        <!-- Footer -->
        {% include './partials/footer.html' %}
    </div>

    <script>
        async function getNewFact() {
            const button = document.querySelector('.fact-generator-button');
            const buttonText = document.getElementById('button-text');
            const factText = document.getElementById('fact-text');
            
            // Show loading state
            buttonText.textContent = 'Loading...';
            button.disabled = true;
            
            try {
                // Call /generate expecting JSON when json=1 query param is present
                const response = await fetch('/generate?json=1', {
                    headers: { 'Accept': 'application/json' }
                });
                let data;
                try {
                    data = await response.json();
                } catch (parseError) {
                    console.error('Error parsing JSON response:', parseError);
                    return;
                }
                
                // Add a small fade effect
                factText.style.opacity = '0.5';
                setTimeout(() => {
                    factText.textContent = data.fact;
                }, 200);
            } catch (error) {
                console.error('Error fetching new fact:', error);
                factText.textContent = 'Sorry, could not load a new fact. Please try again.';
            } finally {
                // Reset button state
                buttonText.textContent = 'New Fact';
                button.disabled = false;
            }
        }
    </script>
</body>
</html>

```
2. Visit `/generate` to see the nicely presented fact.