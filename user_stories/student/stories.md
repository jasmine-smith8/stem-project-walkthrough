# User Stories

## First, let us come up with a project and team name together

`Project Name:` `YOUR NAME`

`Team Name:` `YOUR NAME`

# P0: Random Fun Fact Generator
As an engineer, I want to be able to get a random fun fact from a database, so that I can share them with my team.

---

## Implementation Details

### HTTP Handler (REST)
The handler bridges the database and the User Interface (UI), allowing the random fact generator page to display facts and fetch new ones without having to refresh the page.

#### Steps:
**Create the get_route function** in `rest/get_fact.py`:
   - Import the necessary Flask modules (request, jsonify, render_template)
   - Update the function that calls the database `get_fact` function
   - Check if the request wants JSON format by looking for "json" parameter
   - Return either JSON data or render an HTML template with the fact
   
---

### Database Layer
The database implementation fetches a single random fact from the PostgreSQL database.

#### Steps:
**Create the get_fact function** in `database/get_fact.py`:
   - Import the PostgresConnectionProvider from `database/provider.py`
   - Import the Fact class from `fact.py`
   - Execute a SQL query to select a random fact from the facts table
   - Return a Fact object with the retrieved data, or a "No facts found" message if empty

---

### REST Router
#### Steps:
**Update the router** in `rest/router.py`:
   - Import the get_route function from get_fact module
   - Add a new URL rule for "/generate" that accepts GET requests
   - Connect this route to your get_route function
   - Test by visiting `/generate` on localhost to see a fact in JSON format

---

### Unit Tests
**Create test files** following the pattern `filename_test.py`:
   - Test the happy path (successful fact retrieval)
   - Test edge cases (empty database, connection errors)
   - Place tests in the same directory as the file being tested
   - PowerPoint: Why would we want unit tests to validate functions are working correctly as a software development team?

---

# P1: Random Fun Fact Creator
As an engineer, I want to be able to create my own fun facts, so that I can expand the fact list and never run out of new ones.

---

## Implementation Details

### HTTP Handler (REST)
#### Steps:
**EDIT the create_route function** in `rest/create_fact.py`:
   - Handle both GET and POST requests in the same function
   - For GET requests: render a form template
   - For POST requests: extract the fact text from the form data
   - Validate that the fact text is provided
   - Call the database `create_fact` function
   - Return the template with the newly created fact

---

### Database Layer
#### Steps:
**EDIT the create_fact function** in `database/create_fact.py`:
   - Accept a fact_text parameter
   - Create a database connection
   - Execute an INSERT SQL statement to add the new fact
   - Use RETURNING clause to get the new fact's ID
   - Commit the transaction and return a Fact object

---

### REST Router
#### Steps:
**Update the router** in `rest/router.py`:
   - Import the create_route function
   - Add a new URL rule for "/create" that accepts both GET and POST methods
   - Test by visiting `/create` to see the form and submit new facts

---

### Unit Tests
**Test the create functionality**:
   - Test successful fact creation
   - Test validation (empty fact text)
   - Test database errors

---

# P1: Random Fun Fact Website Design
As a UI/UX engineer, I want my random fun fact generator to provide an accessible user experience whilst maintaining a clear theme.

## Implementation Details

### CSS Implementation
**Customize the stylesheet** in `static/css/styles.css`:
   - Look for `#TASK` comments that indicate customizable areas
   - Update colors, fonts, and layout to match your team's theme
   - Ensure accessibility with proper contrast ratios
   - PowerPoint: What other considerations could we have made to improve user experience?

# P2: Random Fun Fact Voting System
As an engineer, I want to be able to add a voting system to my fact service, so that I can track which facts my team like or dislike.

---

## Implementation Details

### HTTP Handler (REST)
#### Steps:
**Create the vote_route function** in `rest/vote_fact.py`:
   - Handle POST requests with JSON data
   - Extract fact_id and vote_type from the request
   - Call the database vote_fact function
   - Return updated vote counts as JSON
   - Handle errors appropriately

**Update the get_route function** in `rest/get_fact.py`:
   - Include like and dislike counts in both JSON and template responses
   - Pass vote counts to the HTML template

---

### Database Layer
#### Steps:
**Create the vote_fact function** in `database/vote_fact.py`:
   - Accept fact_id and vote_type parameters
   - Update the appropriate vote count (likes or dislikes) in the database
   - Validate the vote_type parameter
   - Return the updated Fact object with current vote counts
   - Handle cases where the fact doesn't exist

---

### REST Router
#### Steps:
**Update the router** in `rest/router.py`:
   - Import the vote_route function
   - Add a new URL rule for "/api/vote" that accepts POST requests
   - This creates an API endpoint for voting functionality

---

### Unit Tests
**Test the voting functionality**:
   - Test successful like and dislike votes
   - Test invalid vote types
   - Test voting on non-existent facts

---

### HTML Integration
**Update the generate template** in `templates/generate.html`:
   - Add like and dislike buttons with vote counts
   - Include JavaScript to handle vote button clicks
   - Update vote counts dynamically without page refresh
   - Display current vote counts for each fact

---

# P2: Random Fun Fact Filter
As an engineer, I want to be able to filter facts by categories, so that I can tailor my facts to the audience.

---

## Implementation Details

### HTTP Handler (REST)
#### Steps:
**Update the get_route function** in `rest/get_fact.py`:
   - Include category information in JSON responses
   - Pass category data to the HTML template

---

### Database Layer
#### Steps:
**Update the get_fact function** in `database/get_fact.py`:
   - Modify the SQL query to include the category column
   - Update the Fact object creation to include category information

---

### HTML Integration
**Update the generate template** in `templates/generate.html`:
   - Display the fact category in the user interface
   - Update JavaScript to handle category information when fetching new facts
   - Style the category display appropriately

---