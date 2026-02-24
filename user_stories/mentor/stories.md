# User Stories

# P0: Random Fun Fact Generator
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
2. Visit `http://127.0.0.1:5000/generate` on localhost to see a fact.

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
<head>
    <title>Random Fact Generator</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
</head>
<div>
    <p>Your random fact is: </p>
    <strong id="fact-text">{{ random_fact }}</strong>
    <button onclick="getNewFact()">New Fact</button>
</div>

<script>
    async function getNewFact() {
        const button = document.querySelector('button');
        const factText = document.getElementById('fact-text');
        
        // Show loading state
        button.textContent = 'Loading...';
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
            
                    factText.textContent = data.fact;
                    factText.textContent = data.fact;
                }, 200);
            factText.textContent = data.fact;
                }, 200);
        } catch (error) {
            console.error('Error fetching new fact:', error);
            factText.textContent = 'Sorry, could not load a new fact. Please try again.';
        } finally {
            // Reset button state
            button.textContent = 'New Fact';
            button.disabled = false;
        }
    }
</script>
```
2. Visit `http://127.0.0.1:5000/generate` to see the nicely presented fact.

# P1: Random Fun Fact Creator
As an engineer, I want to be able to create my own fun facts, so that I can expand the fact list and never run out of new ones.

---

## Implementation Details

### HTTP Handler (REST)
The handler bridges the database layer and the UI layer, allowing the random fact generator page to display facts and fetch new ones without page refreshes. Prior to the implementation of HTML, this will just be a JSON response.

#### Steps:
1. Implement the `create_route()` method in `create_fact.py`.

```python
def create_route():
    if request.method == "GET":
        return render_template("create.html")
        #GET method to render the create form
    if request.method == "POST":
        fact_text = request.form.get("fact_text")
        if not fact_text:
            return "Fact text is required", 400
        fact_create_entity = create_fact(fact_text)
        return render_template("create.html", random_fact=fact_create_entity.fact)
```

---

### Database Layer
The database implementation fetches a single random fact from the PostgreSQL database.

#### Steps:
1. Implement the `create_fact()` method in `create_fact.py`.

```python
def create_fact(fact_text: str) -> Fact:
    provider = PostgresConnectionProvider()
    with provider.cursor() as cur:
        cur.execute(
            "INSERT INTO facts (fact) VALUES (%s) RETURNING id, fact;",
            (fact_text,)
        )
        result = cur.fetchone()
        provider.commit()
        return Fact(id=result[0], fact=result[1])
```

---

### REST Router
#### Steps:
1. Add a `create` route with a `GET` and a `POST` method to `router.py`. 

Both methods are needed: 

- `GET` to render the create fact form on the frontend.
- `POST` to insert the new fact into the database.

```python
from flask import Flask
from .home import home_route
from .get_fact import get_route
from .create_fact import create_route

def create_app():
    app = Flask(__name__,
                template_folder='../templates',
                static_folder='../static')
    app.add_url_rule("/", view_func=home_route, methods=["GET"])
    app.add_url_rule("/generate", view_func=get_route, methods=["GET"])
    app.add_url_rule("/create", view_func=create_route, methods=["GET","POST"]) # TASK
```
2. Visit `http://127.0.0.1:5000/create` on localhost to see a fact.

```
{
    "fact": "Honey never spoils."
}
```
---

### Unit Tests
1. Add unit tests to cover the create fact logic.
2. Place tests in the same directory as the original file, following the convention `filename_test.py`.
3. Reference the given happy path & unit test guide located in the same folder and encourage students to think about negative cases to improve test coverage.

# P2: Random Fun Fact Website Design
As a UI/UX engineer, I want my random fun fact generator to provide an accessible user experience whilst maintaining a clear theme.

## Implementation Details

### P2.1 CSS Implementation

In `static/css/styles.css`, identify areas you would like to update:

 - You will see a `#TASK` comment next to any colour or fonts that can be customised.
 - This task is flexible, so collaborate with your team to come up with a cohesive theme that will fit with your implementation and branding.

# P3: Random Fun Fact Voting System
As an engineer, I want to be able to add a voting system to my fact service, so that I can track which facts my team like or dislike.

---

## Implementation Details

### HTTP Handler (REST)
The handler bridges the database layer and the UI layer, allowing the random fact generator page to display facts and fetch new ones without page refreshes. Prior to the implementation of HTML, this will just be a JSON response.

#### Steps:
1. Implement the `vote_route()` method in `vote_fact.py`.

```python
def vote_route():
    data = request.json
    fact_id = data.get("fact_id")
    vote_type = data.get("vote_type")

    try:
        updated_fact = vote_fact(fact_id, vote_type)
        
        new_count = updated_fact.likes if vote_type == 'like' else updated_fact.dislikes
        
        response = {
            "fact_id": updated_fact.id,
            "new_count": new_count,
            "likes": updated_fact.likes,
            "dislikes": updated_fact.dislikes
        }
        return jsonify(response), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
```

---

2. Update the `get_route()` method in `get_fact.py`.

```python
def get_route():
    fact = get_fact()
    wants_json = request.args.get("json") in ("1", "true", "True")
    if wants_json:
        return jsonify({
            "id": getattr(fact, "id", None),
            "fact": fact.fact,
            "likes": getattr(fact, "likes", 0), #TASK
            "dislikes": getattr(fact, "dislikes", 0) #TASK
        })
    return render_template("generate.html",
                         random_fact=fact.fact,
                         random_fact_id=fact.id,
                         random_fact_likes=getattr(fact, "likes", 0), #TASK
                         random_fact_dislikes=getattr(fact, "dislikes", 0)) #TASK
```

---

### Database Layer
The database implementation fetches a single random fact from the PostgreSQL database.

#### Steps:
1. Implement the `vote_fact()` method in `vote_fact.py`.

```python
def vote_fact(fact_id: int, vote_type: str) -> Fact:
    provider = PostgresConnectionProvider()
    with provider.cursor() as cur:
        if vote_type == "like":
            cur.execute(
                "UPDATE facts SET likes = likes + 1 WHERE id = %s;",
                (fact_id,)
            )
        elif vote_type == "dislike":
            cur.execute(
                "UPDATE facts SET dislikes = dislikes + 1 WHERE id = %s;",
                (fact_id,)
            )
        else:
            raise ValueError("Invalid vote type")

        cur.execute(
            "SELECT id, fact, category, likes, dislikes FROM facts WHERE id = %s;",
            (fact_id,)
        )
        result = cur.fetchone()
        provider.commit()
        if result:
            return Fact(id=result[0], fact=result[1], category=result[2], likes=result[3], dislikes=result[4])
        else:
            raise ValueError("Fact not found")
```

---

### REST Router
#### Steps:
1. Add an `api/vote` route with a `POST` method to `router.py`. 

- `POST` to insert the vote into the database.

```python
from flask import Flask
from .home import home_route
from .get_fact import get_route
from .create_fact import create_route

def create_app():
    app = Flask(__name__,
                template_folder='../templates',
                static_folder='../static')
    app.add_url_rule("/", view_func=home_route, methods=["GET"])
    app.add_url_rule("/generate", view_func=get_route, methods=["GET"])
    app.add_url_rule("/create", view_func=create_route, methods=["GET","POST"]) 
    app.add_url_rule("/api/vote", view_func=vote_route, methods=["POST"]) # TASK

    # Print all registered routes
    print("Registered routes:")
    for rule in app.url_map.iter_rules():
        print(f"{rule} -> {rule.methods}")
    return app
```

### Unit Tests
1. Add unit tests to cover the vote fact logic.
2. Place tests in the same directory as the original file, following the convention `filename_test.py`.
3. Reference the given happy path & unit test guide located in the same folder and encourage students to think about negative cases to improve test coverage.

---

### HTML Integration
1. Add HTML in order to create a form, which will be used to enter in the fact data.

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
            <div class="voting-container">
            <div class="vote-section">
                <button class="vote-button like-button" onclick="vote('like', '{{ random_fact_id }}')">
                <img src="{{ url_for('static', filename='images/thumbs-up.jpg') }}" alt="Like" class="vote-icon">
                </button>
                <span id="like-count-{{ random_fact_id }}" class="vote-count">{{ random_fact_likes }}</span>
            </div>
            <div class="vote-section">
                <button class="vote-button dislike-button" onclick="vote('dislike', '{{ random_fact_id }}')">
                <img src="{{ url_for('static', filename='images/thumbs-up.jpg') }}" alt="Dislike" class="vote-icon">
                </button>
                <span id="dislike-count-{{ random_fact_id }}" class="vote-count">{{ random_fact_dislikes }}</span>
            </div>
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
                    
                    // Update voting counts and button attributes for the new fact
                    const likeButton = document.querySelector('.like-button');
                    const dislikeButton = document.querySelector('.dislike-button');
                    const likeCount = document.querySelector('[id^="like-count-"]');
                    const dislikeCount = document.querySelector('[id^="dislike-count-"]');
                    
                    // Update the onclick attributes with new fact ID
                    likeButton.setAttribute('onclick', `vote('like', '${data.id}')`);
                    dislikeButton.setAttribute('onclick', `vote('dislike', '${data.id}')`);
                    
                    // Update the count element IDs and values
                    likeCount.id = `like-count-${data.id}`;
                    likeCount.textContent = data.likes;
                    dislikeCount.id = `dislike-count-${data.id}`;
                    dislikeCount.textContent = data.dislikes;
                    
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
    <script>
        async function vote(type, factId) {
            if (!factId) {
                console.error('No fact ID provided');
                return;
            }
            const url = '/api/vote';
            const likeCount = document.getElementById(`like-count-${factId}`);
            const dislikeCount = document.getElementById(`dislike-count-${factId}`);

            try {
                const response = await fetch(url, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ fact_id: factId, vote_type: type })
                });

                if (!response.ok) {
                    const errorData = await response.json();
                    console.error('Error voting:', errorData.error);
                    return;
                }

                const data = await response.json();
                if (type === 'like') {
                    likeCount.textContent = data.new_count;
                } else {
                    dislikeCount.textContent = data.new_count;
                }
            } catch (error) {
                console.error('Error voting:', error);
            }
        }
    </script>
</body>
</html>

```
2. Visit `http://127.0.0.1:5000/generate` and your voting buttons should appear below the fact with number of votes.

# P4: Random Fun Fact Filter
As an engineer, I want to be able to filter facts by categories, so that I can tailor my facts to the audience.

---

## Implementation Details

### HTTP Handler (REST)
The handler bridges the database layer and the UI layer, allowing the random fact generator page to display facts and fetch new ones without page refreshes. 

#### Steps:
1. Update the `get_route()` method in `get_fact.py`.

```python
def get_route():
    fact = get_fact()
    wants_json = request.args.get("json") in ("1", "true", "True")
    if wants_json:
        return jsonify({
            "id": getattr(fact, "id", None),
            "fact": fact.fact,
            "category": getattr(fact, "category", None), #TASK
            "likes": getattr(fact, "likes", 0),
            "dislikes": getattr(fact, "dislikes", 0) 
        })
    return render_template("generate.html",
                         random_fact=fact.fact,
                         category=fact.category, #TASK
                         random_fact_id=fact.id,
                         random_fact_likes=getattr(fact, "likes", 0),
                         random_fact_dislikes=getattr(fact, "dislikes", 0))
```

---

### Database Layer
The database implementation fetches a single random fact from the PostgreSQL database.

#### Steps:
1. Update the `get_fact()` method in `get_fact.py`.

```python
def get_fact() -> Fact:
    provider = PostgresConnectionProvider()
    with provider.cursor() as cur:    #TASK
        cur.execute("SELECT id, fact, category, likes, dislikes FROM facts ORDER BY RANDOM() LIMIT 1;")
        result = cur.fetchone()
        if result:                                      #TASK
            return Fact(id=result[0], fact=result[1], category=result[2], likes=result[3], dislikes=result[4])
        else:                                           #TASK
            return Fact(id=None, fact="No facts found.", category="none", likes=0, dislikes=0)
```

---

### Unit Tests
1. Add unit tests to cover the fact filtering logic.
2. Place tests in the same directory as the original file, following the convention `filename_test.py`.
3. Reference the given happy path & unit test guide located in the same folder and encourage students to think about negative cases to improve test coverage.

---

### HTML Integration
1. Add HTML in order to create a form, which will be used to enter in the fact data.

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
                <p>Your random <strong id="fact-category">{{ category }}</strong> fact is: </p>
                <strong id="fact-text">{{ random_fact }}</strong>
            </div>
            <div class="voting-container">
            <div class="vote-section">
                <button class="vote-button like-button" onclick="vote('like', '{{ random_fact_id }}')">
                <img src="{{ url_for('static', filename='images/thumbs-up.jpg') }}" alt="Like" class="vote-icon">
                </button>
                <span id="like-count-{{ random_fact_id }}" class="vote-count">{{ random_fact_likes }}</span>
            </div>
            <div class="vote-section">
                <button class="vote-button dislike-button" onclick="vote('dislike', '{{ random_fact_id }}')">
                <img src="{{ url_for('static', filename='images/thumbs-up.jpg') }}" alt="Dislike" class="vote-icon">
                </button>
                <span id="dislike-count-{{ random_fact_id }}" class="vote-count">{{ random_fact_dislikes }}</span>
            </div>
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
                    const categoryEl = document.getElementById('fact-category');
                    if (categoryEl) categoryEl.textContent = data.category || 'Uncategorized';
                    factText.style.opacity = '1';
                    
                    // Update voting counts and button attributes for the new fact
                    const likeButton = document.querySelector('.like-button');
                    const dislikeButton = document.querySelector('.dislike-button');
                    const likeCount = document.querySelector('[id^="like-count-"]');
                    const dislikeCount = document.querySelector('[id^="dislike-count-"]');
                    
                    // Update the onclick attributes with new fact ID
                    likeButton.setAttribute('onclick', `vote('like', '${data.id}')`);
                    dislikeButton.setAttribute('onclick', `vote('dislike', '${data.id}')`);
                    
                    // Update the count element IDs and values
                    likeCount.id = `like-count-${data.id}`;
                    likeCount.textContent = data.likes;
                    dislikeCount.id = `dislike-count-${data.id}`;
                    dislikeCount.textContent = data.dislikes;
                    
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
    <script>
        async function vote(type, factId) {
            if (!factId) {
                console.error('No fact ID provided');
                return;
            }
            const url = '/api/vote';
            const likeCount = document.getElementById(`like-count-${factId}`);
            const dislikeCount = document.getElementById(`dislike-count-${factId}`);

            try {
                const response = await fetch(url, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ fact_id: factId, vote_type: type })
                });

                if (!response.ok) {
                    const errorData = await response.json();
                    console.error('Error voting:', errorData.error);
                    return;
                }

                const data = await response.json();
                if (type === 'like') {
                    likeCount.textContent = data.new_count;
                } else {
                    dislikeCount.textContent = data.new_count;
                }
            } catch (error) {
                console.error('Error voting:', error);
            }
        }
    </script>
</body>
</html>

```
2. Visit `http://127.0.0.1:5000/generate` and your fact should appear with a category.


