from app import db, Question, app
import os

print("Current working directory:", os.getcwd())
print("Database file path:", os.path.abspath('questions.db'))

with app.app_context():
    db.drop_all()  # Drop existing tables to start fresh
    db.create_all()  # Create new tables

    # Python skill questions - Beginner Level
    python_beginner_questions = [
        Question(skill="Python", level="Beginner", text="What is a variable?",
                options="A storage location, A function, A loop, A class", answer="A storage location", topic="variables"),
        Question(skill="Python", level="Beginner", text="What is the correct way to create a list?",
                options="[] or list(), {} or dict(), () or tuple(), <> or set()", answer="[] or list()", topic="data_types"),
        Question(skill="Python", level="Beginner", text="Which operator is used for exponentiation?",
                options="**, ^, ^^, exp()", answer="**", topic="operators"),
        Question(skill="Python", level="Beginner", text="What is the output of 'Hello {}'.format('World')?",
                options="Hello World, Hello {World}, Hello, Error", answer="Hello World", topic="strings"),
        Question(skill="Python", level="Beginner", text="How do you comment a single line in Python?",
                options="#, //, /* */, --", answer="#", topic="syntax"),
        Question(skill="Python", level="Beginner", text="What is the correct way to create a string?",
                options="Using quotes, Using brackets, Using parentheses, Using curly braces", answer="Using quotes", topic="data_types"),
        Question(skill="Python", level="Beginner", text="Which method is used to add an item to a list?",
                options="append(), add(), insert(), push()", answer="append()", topic="data_types"),
        Question(skill="Python", level="Beginner", text="What is the result of 5 / 2 in Python 3?",
                options="2.5, 2, 2.0, Error", answer="2.5", topic="operators"),
        Question(skill="Python", level="Beginner", text="How do you get the length of a string?",
                options="len(), length(), size(), count()", answer="len()", topic="functions"),
        Question(skill="Python", level="Beginner", text="What is the correct way to check if a key exists in a dictionary?",
                options="in operator, exists(), has_key(), contains()", answer="in operator", topic="data_types")
    ]

    # Python skill questions - Intermediate Level
    python_intermediate_questions = [
        Question(skill="Python", level="Intermediate", text="How do you handle exceptions?",
                options="Try-except, If-else, For-loop, While-loop", answer="Try-except", topic="error_handling"),
        Question(skill="Python", level="Intermediate", text="What is a list comprehension?",
                options="A concise way to create lists, A type of loop, A function, A class", answer="A concise way to create lists", topic="loops"),
        Question(skill="Python", level="Intermediate", text="What is the purpose of the 'self' parameter?",
                options="Refers to the instance of the class, Creates a new instance, Deletes an instance, Imports a module", answer="Refers to the instance of the class", topic="classes"),
        Question(skill="Python", level="Intermediate", text="What is the difference between == and is?",
                options="== compares values, is compares object identity, They are the same, == is for strings only", answer="== compares values, is compares object identity", topic="operators"),
        Question(skill="Python", level="Intermediate", text="What is a generator in Python?",
                options="A function that yields values, A type of loop, A data structure, A class", answer="A function that yields values", topic="functions"),
        Question(skill="Python", level="Intermediate", text="What is the purpose of the __init__ method?",
                options="Constructor method, Destructor method, Main method, Helper method", answer="Constructor method", topic="classes"),
        Question(skill="Python", level="Intermediate", text="What is the difference between append() and extend()?",
                options="append adds one item, extend adds multiple items, They are the same, append is for lists only", answer="append adds one item, extend adds multiple items", topic="data_types"),
        Question(skill="Python", level="Intermediate", text="What is the purpose of the 'with' statement?",
                options="Context management, Loop control, Function definition, Class definition", answer="Context management", topic="error_handling"),
        Question(skill="Python", level="Intermediate", text="What is the difference between a list and a tuple?",
                options="Lists are mutable, tuples are immutable, They are the same, Lists are faster", answer="Lists are mutable, tuples are immutable", topic="data_types"),
        Question(skill="Python", level="Intermediate", text="What is the purpose of the 'yield' keyword?",
                options="Creates a generator function, Defines a class, Creates a loop, Imports a module", answer="Creates a generator function", topic="functions")
    ]

    # Python skill questions - Advanced Level
    python_advanced_questions = [
        Question(skill="Python", level="Advanced", text="What are decorators in Python?",
                options="Functions modifying functions, Loops, Variables, Classes", answer="Functions modifying functions", topic="functions"),
        Question(skill="Python", level="Advanced", text="What is the Global Interpreter Lock (GIL)?",
                options="A mutex protecting Python objects, A type of loop, A memory manager, A garbage collector", answer="A mutex protecting Python objects", topic="concurrency"),
        Question(skill="Python", level="Advanced", text="What is metaclass in Python?",
                options="A class of a class, A type of variable, A function, A module", answer="A class of a class", topic="classes"),
        Question(skill="Python", level="Advanced", text="What is the purpose of __slots__?",
                options="Memory optimization, Speed optimization, Type checking, Error handling", answer="Memory optimization", topic="optimization"),
        Question(skill="Python", level="Advanced", text="What is the difference between __str__ and __repr__?",
                options="str is for users, repr is for developers, They are the same, str is for printing only", answer="str is for users, repr is for developers", topic="classes"),
        Question(skill="Python", level="Advanced", text="What is the purpose of the 'async' keyword?",
                options="Asynchronous programming, Loop control, Function definition, Class definition", answer="Asynchronous programming", topic="concurrency"),
        Question(skill="Python", level="Advanced", text="What is the purpose of the 'await' keyword?",
                options="Pauses execution until async operation completes, Creates a loop, Defines a function, Imports a module", answer="Pauses execution until async operation completes", topic="concurrency"),
        Question(skill="Python", level="Advanced", text="What is the purpose of the 'property' decorator?",
                options="Creates managed attributes, Creates a class, Creates a function, Creates a loop", answer="Creates managed attributes", topic="classes"),
        Question(skill="Python", level="Advanced", text="What is the purpose of the 'staticmethod' decorator?",
                options="Creates a method that doesn't need instance, Creates a class method, Creates a property, Creates a generator", answer="Creates a method that doesn't need instance", topic="classes"),
        Question(skill="Python", level="Advanced", text="What is the purpose of the 'classmethod' decorator?",
                options="Creates a method that receives the class, Creates a static method, Creates a property, Creates a generator", answer="Creates a method that receives the class", topic="classes")
    ]

    # Data Structures skill questions - Beginner Level
    ds_beginner_questions = [
        Question(skill="Data Structures", level="Beginner", text="What is a stack?",
                options="LIFO structure, FIFO structure, Random access, Key-value pair", answer="LIFO structure", topic="stack"),
        Question(skill="Data Structures", level="Beginner", text="What is a queue?",
                options="FIFO structure, LIFO structure, Random access, Key-value pair", answer="FIFO structure", topic="queue"),
        Question(skill="Data Structures", level="Beginner", text="What is an array?",
                options="Contiguous memory locations, Linked nodes, Tree structure, Graph structure", answer="Contiguous memory locations", topic="arrays"),
        Question(skill="Data Structures", level="Beginner", text="What is a linked list?",
                options="Nodes connected by pointers, Contiguous memory, Tree structure, Graph structure", answer="Nodes connected by pointers", topic="linked_lists"),
        Question(skill="Data Structures", level="Beginner", text="What is the time complexity of accessing an array element?",
                options="O(1), O(n), O(log n), O(n^2)", answer="O(1)", topic="arrays"),
        Question(skill="Data Structures", level="Beginner", text="What is a hash table?",
                options="Key-value pairs with O(1) access, Array of elements, Tree structure, Graph structure", answer="Key-value pairs with O(1) access", topic="hash_tables"),
        Question(skill="Data Structures", level="Beginner", text="What is the purpose of a set?",
                options="Unique elements collection, Ordered elements, Key-value pairs, Tree structure", answer="Unique elements collection", topic="sets"),
        Question(skill="Data Structures", level="Beginner", text="What is a dictionary?",
                options="Key-value pairs, Array of elements, Tree structure, Graph structure", answer="Key-value pairs", topic="hash_tables"),
        Question(skill="Data Structures", level="Beginner", text="What is the time complexity of searching in an unsorted array?",
                options="O(n), O(1), O(log n), O(n^2)", answer="O(n)", topic="arrays"),
        Question(skill="Data Structures", level="Beginner", text="What is the purpose of a tuple?",
                options="Immutable sequence, Mutable sequence, Key-value pairs, Tree structure", answer="Immutable sequence", topic="arrays")
    ]

    # Data Structures skill questions - Intermediate Level
    ds_intermediate_questions = [
        Question(skill="Data Structures", level="Intermediate", text="What is the time complexity of searching in a binary search tree?",
                options="O(log n), O(n), O(1), O(n^2)", answer="O(log n)", topic="trees"),
        Question(skill="Data Structures", level="Intermediate", text="What is a heap?",
                options="Complete binary tree with heap property, Array of elements, Linked list, Graph", answer="Complete binary tree with heap property", topic="trees"),
        Question(skill="Data Structures", level="Intermediate", text="What is the purpose of a trie?",
                options="String storage and retrieval, Number storage, Graph representation, Tree traversal", answer="String storage and retrieval", topic="trees"),
        Question(skill="Data Structures", level="Intermediate", text="What is the time complexity of insertion in a hash table?",
                options="O(1) average, O(n), O(log n), O(n^2)", answer="O(1) average", topic="hash_tables"),
        Question(skill="Data Structures", level="Intermediate", text="What is a circular linked list?",
                options="Last node points to first, First node points to last, Random connections, No connections", answer="Last node points to first", topic="linked_lists"),
        Question(skill="Data Structures", level="Intermediate", text="What is the purpose of a doubly linked list?",
                options="Bidirectional traversal, Faster insertion, Better memory usage, Random access", answer="Bidirectional traversal", topic="linked_lists"),
        Question(skill="Data Structures", level="Intermediate", text="What is the time complexity of heap operations?",
                options="O(log n), O(n), O(1), O(n^2)", answer="O(log n)", topic="trees"),
        Question(skill="Data Structures", level="Intermediate", text="What is the purpose of a skip list?",
                options="Probabilistic balanced structure, Random access, Better memory usage, Faster deletion", answer="Probabilistic balanced structure", topic="linked_lists"),
        Question(skill="Data Structures", level="Intermediate", text="What is the time complexity of union operation in disjoint sets?",
                options="Nearly O(1), O(n), O(log n), O(n^2)", answer="Nearly O(1)", topic="sets"),
        Question(skill="Data Structures", level="Intermediate", text="What is the purpose of a segment tree?",
                options="Range queries, Point queries, Graph traversal, Tree balancing", answer="Range queries", topic="trees")
    ]

    # Data Structures skill questions - Advanced Level
    ds_advanced_questions = [
        Question(skill="Data Structures", level="Advanced", text="What is a self-balancing binary search tree?",
                options="AVL tree, Array, Linked list, Stack", answer="AVL tree", topic="trees"),
        Question(skill="Data Structures", level="Advanced", text="What is the purpose of a B-tree?",
                options="Database indexing, Graph traversal, String matching, Memory management", answer="Database indexing", topic="trees"),
        Question(skill="Data Structures", level="Advanced", text="What is a red-black tree?",
                options="Self-balancing BST with color property, Regular BST, Hash table, Array", answer="Self-balancing BST with color property", topic="trees"),
        Question(skill="Data Structures", level="Advanced", text="What is the purpose of a suffix tree?",
                options="String pattern matching, Number sorting, Graph coloring, Tree balancing", answer="String pattern matching", topic="trees"),
        Question(skill="Data Structures", level="Advanced", text="What is a Fibonacci heap?",
                options="Amortized efficient heap, Regular heap, Hash table, Array", answer="Amortized efficient heap", topic="trees"),
        Question(skill="Data Structures", level="Advanced", text="What is the purpose of a treap?",
                options="Randomized balanced BST, Regular BST, Hash table, Array", answer="Randomized balanced BST", topic="trees"),
        Question(skill="Data Structures", level="Advanced", text="What is a van Emde Boas tree?",
                options="Integer set operations, String operations, Graph operations, Tree operations", answer="Integer set operations", topic="trees"),
        Question(skill="Data Structures", level="Advanced", text="What is the purpose of a splay tree?",
                options="Self-adjusting BST, Regular BST, Hash table, Array", answer="Self-adjusting BST", topic="trees"),
        Question(skill="Data Structures", level="Advanced", text="What is a persistent data structure?",
                options="Maintains history of changes, Regular structure, Temporary structure, Static structure", answer="Maintains history of changes", topic="advanced_concepts"),
        Question(skill="Data Structures", level="Advanced", text="What is the purpose of a rope data structure?",
                options="String manipulation, Number manipulation, Graph manipulation, Tree manipulation", answer="String manipulation", topic="advanced_concepts")
    ]

    # Additional Python skill questions - Beginner Level
    python_beginner_questions.extend([
        Question(skill="Python", level="Beginner", text="What is the output of print('Hello' + ' World')?",
                options="Hello World, HelloWorld, Hello + World, Error", answer="Hello World", topic="strings"),
        Question(skill="Python", level="Beginner", text="What is the result of 10 % 3?",
                options="1, 3, 0.333, Error", answer="1", topic="operators"),
        Question(skill="Python", level="Beginner", text="Which of these is a valid Python boolean value?",
                options="True, true, TRUE, truth", answer="True", topic="data_types"),
        Question(skill="Python", level="Beginner", text="How do you convert a string to lowercase?",
                options="lower(), toLower(), lowercase(), str.lower", answer="lower()", topic="strings"),
        Question(skill="Python", level="Beginner", text="What is the correct way to create an empty list?",
                options="[] or list(), {}, (), None", answer="[] or list()", topic="data_types")
    ])

    # Additional Python skill questions - Intermediate Level
    python_intermediate_questions.extend([
        Question(skill="Python", level="Intermediate", text="What is a lambda function?",
                options="Anonymous function, Named function, Class method, Module", answer="Anonymous function", topic="functions"),
        Question(skill="Python", level="Intermediate", text="What does the zip() function do?",
                options="Aggregates elements from iterables, Compresses files, Creates dictionaries, Sorts lists", 
                answer="Aggregates elements from iterables", topic="functions"),
        Question(skill="Python", level="Intermediate", text="What is the purpose of the *args parameter?",
                options="Pass variable number of arguments, Pass keyword arguments, Define constants, Import modules", 
                answer="Pass variable number of arguments", topic="functions"),
        Question(skill="Python", level="Intermediate", text="What is a dictionary comprehension?",
                options="Creates dictionaries using expressions, Creates lists, Defines classes, Imports modules", 
                answer="Creates dictionaries using expressions", topic="data_types"),
        Question(skill="Python", level="Intermediate", text="What is the purpose of the @property decorator?",
                options="Defines getter methods, Creates instances, Defines classes, Imports modules", 
                answer="Defines getter methods", topic="classes")
    ])

    # Additional Data Structures skill questions - Beginner Level
    ds_beginner_questions.extend([
        Question(skill="Data Structures", level="Beginner", text="What is the difference between a list and an array?",
                options="Arrays are fixed size and homogeneous, Lists are fixed size, Arrays are dynamic, No difference", 
                answer="Arrays are fixed size and homogeneous", topic="arrays"),
        Question(skill="Data Structures", level="Beginner", text="What is the time complexity of appending to a list?",
                options="O(1) amortized, O(n), O(log n), O(n^2)", answer="O(1) amortized", topic="arrays"),
        Question(skill="Data Structures", level="Beginner", text="What is a deque?",
                options="Double-ended queue, Single-ended queue, Stack, Tree", answer="Double-ended queue", topic="queue"),
        Question(skill="Data Structures", level="Beginner", text="What is the main advantage of a hash table?",
                options="O(1) average lookup, O(1) worst case lookup, O(log n) lookup, O(n) lookup", 
                answer="O(1) average lookup", topic="hash_tables"),
        Question(skill="Data Structures", level="Beginner", text="What happens in a stack overflow?",
                options="Push on full stack, Pop from empty stack, Random access, Memory corruption", 
                answer="Push on full stack", topic="stack")
    ])

    # Additional Data Structures skill questions - Intermediate Level
    ds_intermediate_questions.extend([
        Question(skill="Data Structures", level="Intermediate", text="What is a priority queue?",
                options="Queue where higher priority elements are served first, Regular queue, Stack, Array", 
                answer="Queue where higher priority elements are served first", topic="queue"),
        Question(skill="Data Structures", level="Intermediate", text="What is the time complexity of quicksort on average?",
                options="O(n log n), O(n), O(n^2), O(log n)", answer="O(n log n)", topic="sorting"),
        Question(skill="Data Structures", level="Intermediate", text="What is a balanced binary search tree?",
                options="Tree with height difference ≤ 1 between subtrees, Any binary tree, Linked list, Array", 
                answer="Tree with height difference ≤ 1 between subtrees", topic="trees"),
        Question(skill="Data Structures", level="Intermediate", text="What is the purpose of hashing?",
                options="Convert data to fixed size value, Sort data, Store data, Delete data", 
                answer="Convert data to fixed size value", topic="hash_tables"),
        Question(skill="Data Structures", level="Intermediate", text="What is a collision in hash tables?",
                options="Two keys hash to same index, Key not found, Table full, Table empty", 
                answer="Two keys hash to same index", topic="hash_tables")
    ])

    # JavaScript skill questions - Beginner Level
    js_beginner_questions = [
        Question(skill="JavaScript", level="Beginner", text="What is the correct way to declare a variable in modern JavaScript?",
                options="let x = 5, var x = 5, x := 5, x => 5", answer="let x = 5", topic="variables"),
        Question(skill="JavaScript", level="Beginner", text="Which operator is used for strict equality comparison?",
                options="===, ==, =, !=", answer="===", topic="operators"),
        Question(skill="JavaScript", level="Beginner", text="What is the correct way to write a function in JavaScript?",
                options="function myFunc() {}, def myFunc():, void myFunc(), func myFunc()", answer="function myFunc() {}", topic="functions"),
        Question(skill="JavaScript", level="Beginner", text="How do you create an array in JavaScript?",
                options="[], new Array(), array(), makeArray()", answer="[] or new Array()", topic="arrays"),
        Question(skill="JavaScript", level="Beginner", text="What is the typeof operator used for?",
                options="Check data type, Compare values, Create variables, Define functions", answer="Check data type", topic="operators"),
        Question(skill="JavaScript", level="Beginner", text="How do you write a single-line comment in JavaScript?",
                options="// comment, # comment, /* comment */, -- comment", answer="// comment", topic="syntax"),
        Question(skill="JavaScript", level="Beginner", text="What is the result of typeof null?",
                options="object, null, undefined, string", answer="object", topic="data_types"),
        Question(skill="JavaScript", level="Beginner", text="How do you convert a string to a number in JavaScript?",
                options="Number(), parseInt(), parseFloat(), All of these", answer="All of these", topic="data_types"),
        Question(skill="JavaScript", level="Beginner", text="What is the correct way to write an if statement?",
                options="if (condition) {}, if condition:, if condition then, if [condition]", answer="if (condition) {}", topic="control_flow"),
        Question(skill="JavaScript", level="Beginner", text="How do you access the first element of an array?",
                options="array[0], array(1), array.first(), array.get(0)", answer="array[0]", topic="arrays")
    ]

    # JavaScript Intermediate Level
    js_intermediate_questions = [
        Question(skill="JavaScript", level="Intermediate", text="What is a closure in JavaScript?",
                options="Function with access to outer scope, Regular function, Global function, Anonymous function", 
                answer="Function with access to outer scope", topic="functions"),
        Question(skill="JavaScript", level="Intermediate", text="What is the purpose of the 'this' keyword?",
                options="References current object context, Creates new object, Defines class, Imports module", 
                answer="References current object context", topic="objects"),
        Question(skill="JavaScript", level="Intermediate", text="What is event bubbling?",
                options="Event propagation from child to parent, Event stopping, Event creation, Event handling", 
                answer="Event propagation from child to parent", topic="events"),
        Question(skill="JavaScript", level="Intermediate", text="What is a Promise in JavaScript?",
                options="Handles asynchronous operations, Synchronous operation, Regular function, Object method", 
                answer="Handles asynchronous operations", topic="async"),
        Question(skill="JavaScript", level="Intermediate", text="What is destructuring in JavaScript?",
                options="Unpack values from arrays/objects, Create arrays, Define objects, Import modules", 
                answer="Unpack values from arrays/objects", topic="syntax"),
        Question(skill="JavaScript", level="Intermediate", text="What is the spread operator used for?",
                options="Expand elements, Combine arrays, Both A and B, None of these", 
                answer="Both A and B", topic="syntax"),
        Question(skill="JavaScript", level="Intermediate", text="What is the purpose of async/await?",
                options="Handle promises more elegantly, Create functions, Define classes, Import modules", 
                answer="Handle promises more elegantly", topic="async"),
        Question(skill="JavaScript", level="Intermediate", text="What is the Map object used for?",
                options="Key-value pairs with any type key, Regular object, Array storage, Function storage", 
                answer="Key-value pairs with any type key", topic="data_types"),
        Question(skill="JavaScript", level="Intermediate", text="What is the purpose of the 'use strict' directive?",
                options="Enforce stricter parsing/error handling, Create modules, Import code, Export code", 
                answer="Enforce stricter parsing/error handling", topic="syntax"),
        Question(skill="JavaScript", level="Intermediate", text="What is event delegation?",
                options="Handle events on parent for children, Direct event handling, Event creation, Event removal", 
                answer="Handle events on parent for children", topic="events")
    ]

    # JavaScript Advanced Level
    js_advanced_questions = [
        Question(skill="JavaScript", level="Advanced", text="What is a generator function?",
                options="Function that can pause execution, Regular function, Async function, Class method", 
                answer="Function that can pause execution", topic="functions"),
        Question(skill="JavaScript", level="Advanced", text="What is the purpose of Symbol?",
                options="Create unique identifiers, Define variables, Create objects, Import modules", 
                answer="Create unique identifiers", topic="data_types"),
        Question(skill="JavaScript", level="Advanced", text="What is a WeakMap?",
                options="Map with weak references to keys, Regular map, Array type, Object type", 
                answer="Map with weak references to keys", topic="data_types"),
        Question(skill="JavaScript", level="Advanced", text="What is the Proxy object used for?",
                options="Custom behavior for operations, Regular object, Data storage, Function wrapper", 
                answer="Custom behavior for operations", topic="objects"),
        Question(skill="JavaScript", level="Advanced", text="What is the purpose of Web Workers?",
                options="Run scripts in background threads, UI updates, DOM manipulation, Event handling", 
                answer="Run scripts in background threads", topic="concurrency"),
        Question(skill="JavaScript", level="Advanced", text="What is the Reflect API?",
                options="Intercept and define custom operations, Regular API, DOM API, Storage API", 
                answer="Intercept and define custom operations", topic="objects"),
        Question(skill="JavaScript", level="Advanced", text="What is the purpose of TypedArrays?",
                options="Handle binary data, Regular arrays, Object storage, String handling", 
                answer="Handle binary data", topic="data_types"),
        Question(skill="JavaScript", level="Advanced", text="What is the Service Worker API?",
                options="Proxy between app, network, and cache, Regular worker, Web worker, Background task", 
                answer="Proxy between app, network, and cache", topic="api"),
        Question(skill="JavaScript", level="Advanced", text="What is the purpose of the Intl object?",
                options="Language sensitive string comparison, Regular object, Data storage, Type checking", 
                answer="Language sensitive string comparison", topic="internationalization"),
        Question(skill="JavaScript", level="Advanced", text="What is the purpose of SharedArrayBuffer?",
                options="Share memory between threads, Regular array, Data storage, Type checking", 
                answer="Share memory between threads", topic="concurrency")
    ]

    # SQL skill questions - Beginner Level
    sql_beginner_questions = [
        Question(skill="SQL", level="Beginner", text="Which SQL statement is used to retrieve data from a database?",
                options="SELECT, GET, RETRIEVE, FETCH", answer="SELECT", topic="queries"),
        Question(skill="SQL", level="Beginner", text="What is the correct way to select all columns from a table?",
                options="SELECT *, SELECT ALL, SELECT everything, GET *", answer="SELECT *", topic="queries"),
        Question(skill="SQL", level="Beginner", text="Which clause is used to filter records?",
                options="WHERE, FILTER, HAVING, WHEN", answer="WHERE", topic="filtering"),
        Question(skill="SQL", level="Beginner", text="How do you sort results in ascending order?",
                options="ORDER BY column ASC, SORT BY column, ARRANGE BY column, GROUP BY column", answer="ORDER BY column ASC", topic="sorting"),
        Question(skill="SQL", level="Beginner", text="Which statement is used to insert new data into a table?",
                options="INSERT INTO, ADD TO, PUT INTO, PLACE INTO", answer="INSERT INTO", topic="data_manipulation"),
        Question(skill="SQL", level="Beginner", text="What is the purpose of the UPDATE statement?",
                options="Modify existing records, Add new records, Delete records, Create tables", answer="Modify existing records", topic="data_manipulation"),
        Question(skill="SQL", level="Beginner", text="Which operator is used to combine conditions with AND logic?",
                options="AND, &&, +, &", answer="AND", topic="operators"),
        Question(skill="SQL", level="Beginner", text="What is a primary key?",
                options="Unique identifier for records, Foreign key, Index, View", answer="Unique identifier for records", topic="database_design"),
        Question(skill="SQL", level="Beginner", text="Which statement is used to delete data from a table?",
                options="DELETE FROM, REMOVE FROM, DROP FROM, ERASE FROM", answer="DELETE FROM", topic="data_manipulation"),
        Question(skill="SQL", level="Beginner", text="What is the purpose of JOIN?",
                options="Combine rows from tables, Sort data, Filter data, Group data", answer="Combine rows from tables", topic="joins")
    ]

    # SQL Intermediate Level
    sql_intermediate_questions = [
        Question(skill="SQL", level="Intermediate", text="What is a subquery?",
                options="Query nested inside another query, Simple query, Table join, View creation", 
                answer="Query nested inside another query", topic="queries"),
        Question(skill="SQL", level="Intermediate", text="What is the difference between UNION and UNION ALL?",
                options="UNION removes duplicates, No difference, UNION is faster, UNION ALL is invalid", 
                answer="UNION removes duplicates", topic="queries"),
        Question(skill="SQL", level="Intermediate", text="What is the purpose of GROUP BY?",
                options="Group rows sharing a property, Sort data, Filter data, Join tables", 
                answer="Group rows sharing a property", topic="aggregation"),
        Question(skill="SQL", level="Intermediate", text="What is the difference between LEFT and RIGHT JOIN?",
                options="Keeps all records from left/right table, No difference, Affects performance, Changes order", 
                answer="Keeps all records from left/right table", topic="joins"),
        Question(skill="SQL", level="Intermediate", text="What is a foreign key?",
                options="References primary key in another table, Primary key, Index, View", 
                answer="References primary key in another table", topic="database_design"),
        Question(skill="SQL", level="Intermediate", text="What is the purpose of HAVING clause?",
                options="Filter grouped data, Filter all data, Sort data, Join tables", 
                answer="Filter grouped data", topic="filtering"),
        Question(skill="SQL", level="Intermediate", text="What are aggregate functions?",
                options="Perform calculations on groups, Regular functions, Table operations, Data types", 
                answer="Perform calculations on groups", topic="aggregation"),
        Question(skill="SQL", level="Intermediate", text="What is the purpose of EXISTS?",
                options="Check if subquery returns results, Delete data, Update data, Join tables", 
                answer="Check if subquery returns results", topic="queries"),
        Question(skill="SQL", level="Intermediate", text="What is a view in SQL?",
                options="Virtual table based on query result, Physical table, Index, Constraint", 
                answer="Virtual table based on query result", topic="database_design"),
        Question(skill="SQL", level="Intermediate", text="What is the purpose of CASE statement?",
                options="Add conditional logic, Join tables, Filter data, Sort data", 
                answer="Add conditional logic", topic="control_flow")
    ]

    # SQL Advanced Level
    sql_advanced_questions = [
        Question(skill="SQL", level="Advanced", text="What is a stored procedure?",
                options="Prepared SQL code for reuse, Regular query, Table type, View definition", 
                answer="Prepared SQL code for reuse", topic="programming"),
        Question(skill="SQL", level="Advanced", text="What is a trigger in SQL?",
                options="Automatic response to database events, Stored procedure, View, Index", 
                answer="Automatic response to database events", topic="programming"),
        Question(skill="SQL", level="Advanced", text="What is database normalization?",
                options="Organize tables to reduce redundancy, Data backup, Query optimization, Index creation", 
                answer="Organize tables to reduce redundancy", topic="database_design"),
        Question(skill="SQL", level="Advanced", text="What is a transaction in SQL?",
                options="Unit of work that is atomic, Regular query, Table operation, Data type", 
                answer="Unit of work that is atomic", topic="transactions"),
        Question(skill="SQL", level="Advanced", text="What is the purpose of ACID properties?",
                options="Ensure reliable transactions, Query optimization, Data backup, Index management", 
                answer="Ensure reliable transactions", topic="transactions"),
        Question(skill="SQL", level="Advanced", text="What is database partitioning?",
                options="Divide tables into smaller parts, Table joining, Data backup, Index creation", 
                answer="Divide tables into smaller parts", topic="optimization"),
        Question(skill="SQL", level="Advanced", text="What is a deadlock?",
                options="Circular wait for resources, Query timeout, Server error, Data corruption", 
                answer="Circular wait for resources", topic="transactions"),
        Question(skill="SQL", level="Advanced", text="What is query optimization?",
                options="Improve query performance, Data backup, Table design, Index removal", 
                answer="Improve query performance", topic="optimization"),
        Question(skill="SQL", level="Advanced", text="What is the purpose of an index?",
                options="Speed up data retrieval, Store data, Join tables, Filter results", 
                answer="Speed up data retrieval", topic="optimization"),
        Question(skill="SQL", level="Advanced", text="What is database sharding?",
                options="Horizontal database partitioning, Vertical partitioning, Data backup, Table joining", 
                answer="Horizontal database partitioning", topic="optimization")
    ]

    # Machine Learning skill questions - Beginner Level
    ml_beginner_questions = [
        Question(skill="Machine Learning", level="Beginner", text="What is supervised learning?",
                options="Learning with labeled data, Learning without labels, Reinforcement learning, Transfer learning", 
                answer="Learning with labeled data", topic="fundamentals"),
        Question(skill="Machine Learning", level="Beginner", text="What type of problem is predicting house prices?",
                options="Regression, Classification, Clustering, Dimensionality reduction", 
                answer="Regression", topic="problem_types"),
        Question(skill="Machine Learning", level="Beginner", text="What is overfitting?",
                options="Model performs well on training but poorly on new data, Model performs poorly on all data, Model is too simple, Model is unbiased", 
                answer="Model performs well on training but poorly on new data", topic="model_evaluation"),
        Question(skill="Machine Learning", level="Beginner", text="What is the purpose of train-test split?",
                options="Evaluate model performance on unseen data, Speed up training, Reduce memory usage, Simplify the model", 
                answer="Evaluate model performance on unseen data", topic="model_evaluation"),
        Question(skill="Machine Learning", level="Beginner", text="What is feature scaling?",
                options="Normalizing numerical features, Creating new features, Selecting features, Removing features", 
                answer="Normalizing numerical features", topic="preprocessing"),
        Question(skill="Machine Learning", level="Beginner", text="What is cross-validation?",
                options="Technique to assess model performance, Type of neural network, Optimization algorithm, Data cleaning method", 
                answer="Technique to assess model performance", topic="model_evaluation"),
        Question(skill="Machine Learning", level="Beginner", text="What is the purpose of the learning rate?",
                options="Controls how much to adjust model in training, Controls model complexity, Determines input features, Sets output values", 
                answer="Controls how much to adjust model in training", topic="training"),
        Question(skill="Machine Learning", level="Beginner", text="What is a confusion matrix used for?",
                options="Evaluate classification performance, Train neural networks, Process images, Clean data", 
                answer="Evaluate classification performance", topic="model_evaluation"),
        Question(skill="Machine Learning", level="Beginner", text="What is feature engineering?",
                options="Creating new features from existing data, Selecting algorithms, Training models, Testing models", 
                answer="Creating new features from existing data", topic="preprocessing"),
        Question(skill="Machine Learning", level="Beginner", text="What is bias in machine learning?",
                options="Model's tendency to consistently miss patterns, Random error, Overfitting, Perfect prediction", 
                answer="Model's tendency to consistently miss patterns", topic="fundamentals")
    ]

    # Machine Learning Intermediate Level
    ml_intermediate_questions = [
        Question(skill="Machine Learning", level="Intermediate", text="What is gradient descent?",
                options="Optimization algorithm for minimizing error, Classification algorithm, Clustering method, Feature selection", 
                answer="Optimization algorithm for minimizing error", topic="optimization"),
        Question(skill="Machine Learning", level="Intermediate", text="What is regularization?",
                options="Prevent overfitting, Increase model complexity, Speed up training, Feature selection", 
                answer="Prevent overfitting", topic="model_evaluation"),
        Question(skill="Machine Learning", level="Intermediate", text="What is K-fold cross validation?",
                options="Dataset splitting technique, Feature selection, Model architecture, Data cleaning", 
                answer="Dataset splitting technique", topic="model_evaluation"),
        Question(skill="Machine Learning", level="Intermediate", text="What is the bias-variance tradeoff?",
                options="Balance between underfitting and overfitting, Model selection, Feature engineering, Data preprocessing", 
                answer="Balance between underfitting and overfitting", topic="model_evaluation"),
        Question(skill="Machine Learning", level="Intermediate", text="What is ensemble learning?",
                options="Combine multiple models, Single model training, Feature selection, Data cleaning", 
                answer="Combine multiple models", topic="algorithms"),
        Question(skill="Machine Learning", level="Intermediate", text="What is the purpose of dropout?",
                options="Prevent neural network overfitting, Speed up training, Feature selection, Data augmentation", 
                answer="Prevent neural network overfitting", topic="neural_networks"),
        Question(skill="Machine Learning", level="Intermediate", text="What is batch normalization?",
                options="Normalize layer inputs, Feature selection, Model selection, Data cleaning", 
                answer="Normalize layer inputs", topic="neural_networks"),
        Question(skill="Machine Learning", level="Intermediate", text="What is transfer learning?",
                options="Reuse pre-trained models, Train from scratch, Feature selection, Data augmentation", 
                answer="Reuse pre-trained models", topic="techniques"),
        Question(skill="Machine Learning", level="Intermediate", text="What is the purpose of learning rate scheduling?",
                options="Adjust learning rate during training, Feature selection, Model selection, Data preprocessing", 
                answer="Adjust learning rate during training", topic="optimization"),
        Question(skill="Machine Learning", level="Intermediate", text="What is early stopping?",
                options="Stop training to prevent overfitting, Speed up training, Feature selection, Data cleaning", 
                answer="Stop training to prevent overfitting", topic="model_evaluation")
    ]

    # Machine Learning Advanced Level
    ml_advanced_questions = [
        Question(skill="Machine Learning", level="Advanced", text="What is backpropagation through time?",
                options="Training algorithm for RNNs, Regular backpropagation, Forward propagation, Feature selection", 
                answer="Training algorithm for RNNs", topic="neural_networks"),
        Question(skill="Machine Learning", level="Advanced", text="What is the vanishing gradient problem?",
                options="Gradients become too small in deep networks, Model complexity, Feature selection, Data preprocessing", 
                answer="Gradients become too small in deep networks", topic="neural_networks"),
        Question(skill="Machine Learning", level="Advanced", text="What is attention mechanism?",
                options="Focus on relevant parts of input, Regular neural network, Feature selection, Data preprocessing", 
                answer="Focus on relevant parts of input", topic="neural_networks"),
        Question(skill="Machine Learning", level="Advanced", text="What is generative adversarial network?",
                options="Two networks competing with each other, Single network, Feature selection, Data preprocessing", 
                answer="Two networks competing with each other", topic="neural_networks"),
        Question(skill="Machine Learning", level="Advanced", text="What is reinforcement learning?",
                options="Learning through environment interaction, Supervised learning, Unsupervised learning, Transfer learning", 
                answer="Learning through environment interaction", topic="techniques"),
        Question(skill="Machine Learning", level="Advanced", text="What is the purpose of LSTM cells?",
                options="Handle long-term dependencies, Regular neural network, Feature selection, Data preprocessing", 
                answer="Handle long-term dependencies", topic="neural_networks"),
        Question(skill="Machine Learning", level="Advanced", text="What is autoencoder?",
                options="Network learning efficient data coding, Classification network, Regression network, Feature selection", 
                answer="Network learning efficient data coding", topic="neural_networks"),
        Question(skill="Machine Learning", level="Advanced", text="What is meta-learning?",
                options="Learning to learn, Regular learning, Transfer learning, Feature selection", 
                answer="Learning to learn", topic="techniques"),
        Question(skill="Machine Learning", level="Advanced", text="What is one-shot learning?",
                options="Learn from one example, Regular learning, Transfer learning, Feature selection", 
                answer="Learn from one example", topic="techniques"),
        Question(skill="Machine Learning", level="Advanced", text="What is federated learning?",
                options="Distributed training preserving privacy, Centralized training, Transfer learning, Feature selection", 
                answer="Distributed training preserving privacy", topic="techniques")
    ]

    # Add all questions to the database
    all_questions = (python_beginner_questions + python_intermediate_questions + python_advanced_questions +
                    ds_beginner_questions + ds_intermediate_questions + ds_advanced_questions +
                    js_beginner_questions + js_intermediate_questions + js_advanced_questions +
                    sql_beginner_questions + sql_intermediate_questions + sql_advanced_questions +
                    ml_beginner_questions + ml_intermediate_questions + ml_advanced_questions)
    
    for question in all_questions:
        db.session.add(question)

    db.session.commit()

    questions = Question.query.all()
    print(f"Number of questions in the database: {len(questions)}")
    for q in questions:
        print(f"Skill: {q.skill}, Level: {q.level}, Topic: {q.topic}, Question: {q.text}")

    print("Questions added to the database successfully!")