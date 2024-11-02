---
layout: post
title: Where programming is going
date: 2024-09-01T00:00:00.001-05:00
author: Douglas Hindson
tags:
  - projects
modified_time: 2024-09-01T00:00:00.001-05:00
---
Programming feels different now.

I feel like a kid who just found out how to copy/paste text on a computer. I don't want to write with a pen or pencil anymore, I think to myself,

"In the future when I use computers for everything, I'll only ever type a word once, then I'll just copy/paste it every time I need that word again!"

When I program alongside LLMs, it feels like I'm throwing away the high-level code I wrote and keeping the compiled machine code. The improvements seemed pretty obvious to me, so I explored a bit to see where the software development industry has landed. It seems like things are still up in the air, it hasn't landed yet.

[insert picture illustration]

I still want to know where things are going, so I looked into the history of programming languages, then I used the history to extrapolate what might happen in the industry going forwards. This post is about what I found.

1. Cultural history of programming languages
2. Projected future of programming languages
3. Wrap-up

## Cultural history of programming languages

### 1. Early Assembly Language (1940s-1950s)
   - **Technological Context**: The first computers, like the ENIAC (1945) and the Manchester Mark I (1948), were programmed using machine code, a binary representation directly understood by the computer's hardware. Assembly language was developed soon after, providing symbolic representations of these binary instructions, making it slightly more human-readable but still hardware-specific.
   - **Cultural Impact**: Early programmers were typically engineers or mathematicians who had a deep understanding of hardware. The culture was one of exclusivity, where programming was a highly specialized skill requiring intimate knowledge of the machine.
   - **Example assembly code for factorial calculation on IBM 704**:
   
```
 CLA   5        # Load the value 5 into the accumulator (initial number to calculate factorial)
 STO   N        # Store the value into memory location N
 L     ONE      # Load 1 into the accumulator (initial result)
 STO   FACT     # Store the accumulator value into memory location FACT

LOOP     L     FACT     # Load FACT into the accumulator
 MUL   N        # Multiply by the value of N
 STO   FACT     # Store result back into FACT
 L     N        # Load N into the accumulator
 SUB   ONE      # Subtract 1
 STO   N        # Store the decremented value of N back
 CLE            # Clear the extension register (for handling overflow)
 TZE   DONE     # If N is now zero, jump to DONE
 TRA   LOOP     # Else, jump back to LOOP

DONE     HPR             # Halt program execution

N        BSS   1        # Memory location for N
FACT     BSS   1        # Memory location for FACT
ONE      DC    1        # Constant value 1
```
   - **Code-culture commentary:** early assembly languages required intimate knowledge of hardware instructions, making programming highly specialized.

### 2. The Birth of High-Level Languages (1950s)
   - **Technological Context**: FORTRAN (FORmula TRANslation, 1954) was the first widely used high-level programming language. COBOL (Common Business-Oriented Language, 1959) emphasized readability and was designed for data processing.
   - **Cultural Shift**: This period marked a democratization of programming. As these high-level languages emerged, more people from non-engineering backgrounds began to engage in programming, fostering a broader and more diverse culture of computing.
   - **Example FORTRAN Code**:

```fortran
   PROGRAM Factorial
       INTEGER :: N, FACTORIAL
       N = 5
       FACTORIAL = 1
       DO I = 1, N
           FACTORIAL = FACTORIAL * I
       END DO
       PRINT *, 'Factorial of', N, 'is', FACTORIAL
   END PROGRAM Factorial
   ```
   - **Code-culture commentary:** FORTRAN abstracts away much of the hardware detail, allowing the focus to shift to solving the problem itself. This opened programming to scientists and engineers who didn't need deep hardware knowledge.

### 3. Standardization and Compiler Advances (1960s-1970s)
   - **Technological Context**: ALGOL (1960) introduced concepts like structured programming and recursion. C (1972) had portability, power, and efficiency that made it foundational for system software, including operating systems like UNIX.
   - **Cultural Development**: The rise of C and UNIX represented a shift toward a culture of portability and openness in computing. The idea that software could be independent of the hardware on which it ran became more widely accepted.
   - **Example C Code and Compilation**:

```c
   #include <stdio.h>

   int factorial(int n) {
       int result = 1;
       for (int i = 1; i <= n; ++i) {
           result *= i;
       }
       return result;
   }

   int main() {
       int n = 5;
       printf("Factorial of %d is %d\n", n, factorial(n));
       return 0;
   }
   ```
   ##### Compile and run across platforms
- PDP-11 with UNIX Version 5 or 6 (Early to Mid-1970s)
- IBM System/370 with UNIX Version 6 (Late 1970s)
- DEC VAX-11/780 with UNIX Version 7 (Late 1970s)

```bash
   cc factorial.c -o factorial
   ./factorial
   Factorial of 5 is 120
   ```

   - **Code-culture commentary:** The portability of C allowed code to be compiled and run on multiple platforms, making it a major step toward software independence from hardware.

### 4. The Advent of Object-Oriented Programming (OOP) (1970s-1980s)
   - Technological Context**: Smalltalk (1972) pioneered the concept of object-oriented programming, while C++ (1983) brought OOP concepts into the mainstream by building on C.
   - **Cultural Impact**: Object-oriented programming altered the way developers conceptualized problems, emphasizing collaboration, modularity, and reusability. It marked the beginning of software engineering as a discipline, with structured methodologies and best practices.
   - **Example C++ Code**:

   ```cpp
#include <iostream.h>

class FactorialCalculator {
    int n;  // Class members were often declared without as much emphasis on encapsulation

public:
    void setNumber(int number) {
        n = number;
    }

    int calculate() {
        int result = 1;
        for (int i = 1; i <= n; i++) {
            result *= i;
        }
        return result;
    }
};

int main() {
    FactorialCalculator calculator;
    int n = 5;

    calculator.setNumber(n);
    cout << "Factorial of " << n << " is " << calculator.calculate() << "\n";

    return 0;
}

   ```
- **Code-culture commentary:** C++ introduced object-oriented programming, allowing programmers to think in terms of objects and methods. This was a major shift toward modularity and real-world problem modelling.

### 5. The Rise of Scripting and Interpreted Languages (1990s)
   - **Technological Context**: languages like Python (1991), Perl (1987), and JavaScript (1995) became easier to use and more flexible. Java (1995) promised "write once, run anywhere," contributing to a surge in cross-platform development.
   - **Cultural Shift**: The 1990s saw the rise of internet culture, and with it, a surge of interest in programming from hobbyists, web developers, and non-traditional programmers. Open-source communities flourished, leading to collaborative development models.
   - **Example Python Code**:

```python
import Numeric  # The predecessor to NumPy

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Create a 3x3 matrix where each element is the factorial of its (row + column) index
matrix_size = 3
factorial_matrix = Numeric.zeros((matrix_size, matrix_size), 'l')

for row in range(matrix_size):
    for col in range(matrix_size):
        factorial_matrix[row][col] = factorial(row + col + 1)
   ```

- **Code-culture commentary:** Python made programming more accessible than ever, emphasizing readability and ease of use. It allowed non-specialists to quickly write powerful programs, reflecting the growth of open-source and collaborative development.

### 6. The Dominance of Frameworks and Libraries (2000s)
   - **Technological Context**: an explosion of frameworks (e.g., Ruby on Rails, Django, .NET) and libraries in the 2000s abstracted away even more complexity.
   - **Cultural Development**: The notion of "standing on the shoulders of giants" became prevalent, as developers could leverage vast ecosystems of existing tools and libraries. This period marked the beginning of the “full-stack developer” era, where individual programmers could build entire applications using pre-built components.
   - **Example Django (Python) Code**:
	   - **Model (models.py)**

     ```python
     # models.py
     from django.db import models

     class Calculation(models.Model):
         number = models.IntegerField()
         result = models.IntegerField()
     ```
     
	   - **View (views.py)**

     ```python
     # views.py
     from django.shortcuts import render
     from .models import Calculation

     def factorial_view(request):
         number = int(request.GET.get('number', 5))
         result = 1
         for i in range(1, number + 1):
             result *= i
         Calculation.objects.create(number=number, result=result)
         return render(request, 'factorial.html', {'number': number, 'result': result})
     ```

	   - **Template (factorial.html)**

     ```html
     <!-- factorial.html -->
     <h1>Factorial Calculation</h1>
     <p>The factorial of {{ number }} is {{ result }}</p>
     ```
- **Code-culture commentary:** Using Django, the complexity of setting up web servers, handling HTTP requests, and managing databases is abstracted away. This demonstrates how frameworks enable developers to focus on business logic instead of reinventing foundational elements, showing a move towards higher levels of abstraction and rapid development.

### 7. The Age of Declarative and Functional Paradigms (2010s)
   - **Technological Context**: languages and frameworks that emphasize "what to do" instead of "how to do it," such as SQL, HTML, and modern web frameworks like React, gained popularity. Functional languages like Haskell, Scala, and Elixir regained interest.
   - **Cultural Shift**: The industry began emphasizing developer productivity, maintainability, and the need to manage complex systems gracefully. The shift toward declarative paradigms mirrored a desire to abstract away underlying complexities further.
   - **Example React (JSX) Code**:

   ```jsx
   // Factorial.js
   import React, { useState } from 'react';

   const Factorial = () => {
     const [number, setNumber] = useState(5);
     const [result, setResult] = useState(1);

     const calculateFactorial = (n) => {
       let res = 1;
       for (let i = 1; i <= n; i++) {
         res *= i;
       }
       return res;
     };

     const handleChange = (e) => {
       const value = parseInt(e.target.value, 10) || 1;
       setNumber(value);
       setResult(calculateFactorial(value));
     };

     return (
       <div>
         <h1>Factorial Calculator</h1>
         <input
           type="number"
           value={number}
           onChange={handleChange}
           min="1"
         />
         <p>The factorial of {number} is {result}</p>
       </div>
     );
   };

   export default Factorial;
   ```
- **Code-culture commentary:** React's adoption represented a shift where front-end development became less about manipulating individual DOM elements and more about managing the overall state of an application. This change mirrored a cultural evolution toward building highly interactive user experiences with code that was not just functional but also inherently easier to reason about and collaborate on, reducing the cognitive overhead of handling intricate browser behaviors directly.

## Projected future of programming languages

### Key developments in the past
- Evolution of abstraction layers
- Growth of domain-specific languages (DSLs)
- Emergence of shared protocols
- Democratization of programming
- Cultural shifts toward collaboration and open source
### 1. Evolution of abstraction layers

#### What happened before

The shift from assembly language to high-level languages like FORTRAN and COBOL marked a dramatic increase in abstraction. This evolution allowed developers to focus more on problem-solving and less on hardware-specific details.

#### What could happen again: natural language programming & intent-based programming

- **Natural Language Programming**: Just as early high-level languages made it easier for engineers to express complex logic, the next generation of languages could harness natural language more effectively, allowing developers to describe software behavior in plain human language. Tools like OpenAI's Codex and GitHub Copilot are precursors, but we might see integrated development environments (IDEs) where programming and documentation merge seamlessly, reducing the distinction between code and natural language instructions.
  
- **Intent-Based Programming**: Moving from "how" to "what," we could see languages that allow developers to define end goals, with the system handling the specifics. This approach would echo the rise of declarative programming but at a much more sophisticated level, where intent and constraints become the primary means of interaction.

##### Future LLM-oriented approach

```markdown
You are a software engineer building a personal application.

Create a simple web app that takes a number as input and calculates its factorial. After the user submits the number, display the result below the input field with the text 'The factorial of {n} is {result}'. Style the web page with a blue header and centered input field.

Make the app have a frontend and a backend so that further functions can be added to both.

Identify incorrect inputs and respond to them appropriately.

Identify the few tests that ensure the app behaviours are working as expected and write them.

Write the code, run the tests, deploy it locally, then test that the deployment is working properly.
```

**Commentary:** Here, the developer only needs to specify the goals of the software, and the system automatically handles the translation into executable code. This echoes the abstraction seen in early high-level languages but at a much more sophisticated level.

### 2. Growth of domain-specific languages (DSLs)

#### What Happened Before

DSLs like SQL, HTML, and CSS emerged to address specific problem domains, allowing users to interact with computers in more intuitive, task-oriented ways.

#### What could happen again: niche DSLs & multi-modal DSLs

- **AI-Augmented DSLs**: The next generation might involve more niche DSLs tailored to domains such as finance, healthcare, or manufacturing. DSLs would enable software and AI to more effective engage in those domains.
  
- **Multi-Modal DSLs**: We might see DSLs that blend different media (text, voice, images) for more intuitive problem-solving. For instance, a data analyst could draw a diagram and annotate it with natural language, with the system converting this input into a structured, executable data transformation pipeline.

##### Future niche DSL approach:

Imagine a supply chain management DSL that blends declarative, graph-based, and constraint-oriented paradigms.
```supply
# Define the supply chain graph
GRAPH 'FullSupplyChain' {
  NODE 'SupplierX' {
    PRODUCT: 'Widget A'
    LEAD_TIME: 5 days
  }
  NODE 'Manufacturing' {
    PROCESS: 'Assembly'
    INPUT: 'Widget A'
    OUTPUT: 'Finished Product'
    CAPACITY: calculate_capacity(daily_output=500 units)
  }
  NODE 'Distribution' {
    LOCATION: 'Central Warehouse'
    CAPACITY: 1000 units
  }
  EDGE 'SupplierX' -> 'Manufacturing' {
    TRANSPORT: 'Truck'
    COST: variable_cost(distance)
  }
  EDGE 'Manufacturing' -> 'Distribution'
}

# Plan an optimized supply chain operation
PLAN supply_chain_optimization
  OBJECTIVE minimize total_cost
  CONSTRAINTS {
    delivery_times WITHIN 2 days
    inventory_levels MAINTAIN safety_stock
    demand_forecasts CONSIDER forecast_accuracy
  }

# Simulate and adjust using real-time data
SIMULATE supply_chain_for 60 days
```

**Code-culture commentary:** DSLs will give programming culture more **specialization and accessibility**, allowing experts in specific fields to engage with technology in terms they understand.

### 3. Emergence of shared protocols

#### What happened before

The creation of standardized languages and protocols, such as ANSI C, POSIX, and the ISO standards for languages like SQL, helped unify the computing industry, allowing code to be more portable and interoperable.

#### What could happen again: interoperability standards for AI-driven development

- **Interoperability Standards for AI-Driven Development**: As AI-assisted programming becomes more prevalent, we might see the emergence of standardized interfaces for LLMs, allowing different tools to communicate seamlessly. This development would parallel the standardization seen with programming languages, but applied to AI models, data formats, and intent representations.
  
- **Cross-Platform Natural Language APIs**: Similar to how languages like Java provided a "write once, run anywhere" experience, we could see frameworks where instructions given in natural language are converted into executable code across multiple platforms, allowing non-programmers to interact with different systems without worrying about underlying languages or frameworks.

##### Future approach: cross-platform natural language APIs

In this scenario, you might define a factorial calculation using a standard, natural language API that can run on any system:

```json
{
  "function": "factorial",
  "description": "Calculates the factorial of a number",
  "input": "integer n",
  "logic": [
    {"condition": "n == 0", "return": 1},
    {"return": "n * factorial(n - 1)"}
  ]
}
```

**Commentary:** This JSON-based format could be understood and executed across different platforms and languages, allowing all kinds of things to read and execute the instructions.

### 4. Democratization of programming

#### What Happened Before

The advent of BASIC in the 1960s and the personal computer revolution of the 1980s empowered hobbyists and non-experts to write programs. This democratization led to a surge in creative, diverse software development and a wave of technological innovation.

#### What could happen again: layman development powered by AI

- **Layman Development Powered by AI**: Just as BASIC empowered home computer enthusiasts, AI-driven low-code/no-code platforms could enable a new generation of "layman developers." These tools could become sophisticated enough that individuals without formal programming training could build complex, domain-specific applications, potentially leading to another wave of grassroots innovation.
  
- **Global, Inclusive Programming Communities**: The barrier to entry might drop so low that communities from regions currently underrepresented in software development become major contributors, fostering a more diverse ecosystem of creators. Imagine forums or collaborative platforms where people from different disciplines, speaking different languages, contribute ideas that are instantly translatable into executable code.

##### Future low-code/no-code approach

Imagine a no-code environment operated through voice:

```voice
"Make a calculator app with the factorial function and install it on my phone."
"Make a short video course to explain how it solves the problem I'm working on right now and how it works."
```

**Commentary:** This example illustrates how AI-driven platforms could allow anyone, regardless of technical background, to build and execute complex logic using natural language.

### 5. Cultural shifts toward collaboration and open source

#### What happened before

The rise of UNIX, Linux, and the open-source movement in the late 20th century created a culture of sharing, collaboration, and collective problem-solving. This ethos was fundamental to the success of technologies like the World Wide Web.

#### What could happen again: code libraries as culture artifacts

- **Open-Source AI Models and Knowledge Bases**: As LLMs and AI-driven tools become more integrated into programming, open-source AI models might become the norm, leading to a collaborative culture around improving these systems. We could see shared repositories of "intent patterns" or common knowledge structures that help AI tools better understand and respond to different problem domains. Different patterns might emerge from different cultures.
  
- **Community-Driven Language Evolution**: Just as the open-source community contributes to language development (e.g., Python's PEP process), the next generation might involve real-time, collaborative evolution of AI-driven languages, with users contributing refinements to how the system understands and responds to natural language input.

##### Future open-source cultural library

Developers collaborate on an open-source LLM "snippet" repository, where they define common functions like factorials. You might pull the latest community-optimized version:
[change]
[ex: mix "mom and pop shop" with "Ottawa Valley Canadian"]

```python
# Fetch and execute the latest community version of the factorial function
factorial = get_open_source_function("factorial", "v1.2.3")
result = factorial(5)
```

**Commentary:** The factorial function isn’t just defined by one person—it’s the product of collective knowledge, continuously refined and improved by the community, allowing you to pull and use the best version available.

### 6. The emergence of new programming paradigms

#### What Happened Before

The shift to object-oriented programming (OOP) in the 1980s and the later rise of functional programming introduced new ways of thinking about software design, allowing developers to model problems more effectively.

#### What Could Happen Again: Contextual Programming & Collaborative, Multi-Agent Programming

- **Contextual Programming**: Future languages could leverage context-aware programming, where the development environment understands the broader project context, user preferences, and domain-specific requirements, dynamically adapting code suggestions. This would be an evolution of current IDEs' code completion features, but far more intelligent and responsive to the developer's intent.
  
- **Collaborative, Multi-Agent Programming**: Just as pair programming and agile methodologies emphasized collaboration, the next era might involve working with intelligent agents as co-developers. Programmers could orchestrate multiple AI agents, each specializing in different tasks (e.g., optimizing algorithms, ensuring security, refactoring code), in a collaborative manner.

##### **Future Context-Aware LLM-Oriented IDE Approach:**

Imagine an IDE that understands the context of your entire project and suggests improvements dynamically:

```python
# The IDE understands that we're working on mathematical functions.
# It suggests using memoization to optimize the factorial calculation.
@memoize
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

Or, multiple AI agents might work together:
- One agent handles optimization, another ensures security, while another documents the function. You would simply oversee and guide them.

**Commentary:** This collaborative approach blurs the line between human and machine, allowing for more sophisticated and efficient programming with AI as an active partner.

# This is the beginning of the post
# Everything above this was not real
# This blog post starts here

All that content above I wrote heavily augmented by LLMs. If you got here, you were probably skimming a lot of the content. You can take your attention off of autopilot now. You can actually engage with this next text section before the framework and code sections, because I really wrote this part.

The content above was AI-generated takes on what comes next. Made of ideas that taste like cardboard and water, which feel familiar and plausible-sounding because LLMs are very good at that. Reality is stranger, its direction is unfamiliar and implausible with a bit of watery cardboard mixed in. I'm going to show you a future based on reality - where I wrote all that above text augmented by LLMs. The future below is closer to [how things are trending](https://www.coursera.org/learn/ai-powered-software-and-system-design).

> “The Matrix is surely the kind of film about the matrix that the matrix would have been able to produce.”

> “The actors are in the matrix, that is, in the digitized system of things; or, they are radically outside it, such as in Zion, the city of resistors. But what would be interesting is to show what happens when these two worlds collide. The most embarrassing part of the film is that the new problem posed by simulation is confused with its classical, Platonic treatment.”

[-Jean Baudrillard, 2004](https://baudrillardstudies.ubishops.ca/the-matrix-decoded-le-nouvel-observateur-interview-with-jean-baudrillard/#:~:text=The%20Matrix%20is%20surely%20the%20kind%20of%20film%20about%20the%20matrix%20that%20the%20matrix%20would%20have%20been%20able%20to%20produce.) - the philosopher whose work The Matrix was based upon.

## My WIP writing framework

In [my previous post in this series](./2024-09-01-editing-science-fiction-with-llms), I described a standard writing process. Here's where I'm at now with my LLM-augmented writing process:

1. Write an outline
2. Research
3. Fine-tune a model
4. Generate diamonds in the rough
5. Rewrite outline
6. 'Write' the first draft
7. Refine and rewrite iteratively

I explained an approach to automating writing and how to go about soliciting development edit feedback in the [previous post](./2024-09-01-editing-science-fiction-with-llms). Here, it will be more technical and I will explore:
- "3. Fine-tune a model"
- "4. Generate diamonds in the rough"
- "6. 'Write' the first draft"
- "7. Refine and rewrite iteratively"

### Fine-tune a model

[insert]
[compare examples in prompt vs fine-tuning]
### Generate diamonds in the rough

[It's easier to recognize good content than it is to produce it.](./2024-09-13-recognition-vs-recollection)

There's two ways to generate gems:
- Mass produce, then filter
- Ask the right questions

#### Mass produce, then filter

I use LLMs to generate a lot of text, then I use LLMs to filter for the good stuff, then I pick what I like from the filtered results. 

When a generate text, I might prompt for exposition or dialogue or descriptions. I might include the preceding text and ask it to continue writing. I'll often ask it to cold open a section because I've seen it produce more interesting content that way.

I'll pick out phrases, sentences, or paragraphs and copy it to a temporary file. Up to 5% of text gets copied. So far I've read them all myself, but I'm seeing promising results from prompting a model to filter the text. "Mass produce, then filter" works well with fiction, but I haven't had success with non-fiction yet.

<details markdown="1">
<summary>Here is an example "writer" prompt I wrote for this post (click to expand)</summary>
You are an engineer writing a series of blog posts intended mostly for AI industry folks but also writers. In this article, you are writing about two main topics:
* the history of the industry going from assembly to high-level languages and what that means about the "next generation" of programming languages
* a demonstration of a possible style of the "next generation" of programming languages, which combines the craft of writing with applied ML techniques - the process of how this article was written using LLMs

There are three parts to the overall blog post:
- The hook, to draw the reader in and give a taste of what will be explored in "the history".
- The history, information about the history of development of programming languages and the cultural development around them.
- The future of new programming languages with that history.
- The plot twist, that this blog post was written by AI and the method was nothing like what was described in the future of new programming languages.
- The demo, which explains how this post was written, showing what the future could look like.
- The conclusion, wrapping up the theses in the article and linking to previous posts that explore related topics further.

Think and explain why the audience might connect with this content. Use that reasoning to write a compelling hook and initial transition to "the history". Don't write any of "the history".

Use this as an inspiration for the hook:

I feel like I'm writing code in Python, then throwing all that text away and committing the machine code that comes out. That's what programming with LLMs feels like right now.
</details>

#### Ask the right question

The question I had for this post was, "Where is the industry going in the near-term with new "programming languages" / code management methodologies?" Unsatisfying answers led me to the question, "What have been the cultural changes in programming languages as they evolved?" Here are the prompts and conversations that generated most of the post above:

<details markdown="1">
<summary>Research prompts for this post (click to expand)</summary>
https://chatgpt.com/share/66f025ec-24c4-800f-9c34-3866f089fd48

You are an academic historian of computation with expertise in the history and development of computing technology. I am an engineer seeking a deep understanding of this field. As we engage in this discussion, please provide well-reasoned, detailed, and accurate responses, citing reputable sources whenever possible. If any assumptions or uncertainties arise, make them explicit, and clearly distinguish between verified information and speculation. Prioritize clarity, precision, and evidence-based reasoning in your explanations, and ensure that you provide context when introducing historical events, concepts, or figures.

I am writing a post about a brief history of the transition from low-level programming to where we are today. I want to use that history to illustrate what may happen in the future with LLMs. What are considered to be the main events in the transition from low-level languages to high-level languages? I'm interested both in technological achievements and cultural developments in the computing/high-tech industry.

What indicators suggest or detract from the possibility that we are now transitioning to a next generation of higher-level programming languages?

What technological advancements and cultural phenomena could happen again, but now with the next generation of languages?

---

https://chatgpt.com/share/66f02ecb-7d54-800f-b6a9-54d8e5db069d

You are an engineer writing a series of blog posts intended for AI industry folks and writers. In this article, you are writing about two main topics:
* the history of the industry going from assembly to high-level languages and what that means about the "next generation" of programming languages
* a demonstration of a possible style of the "next generation" of programming languages, which combines the craft of writing with applied ML techniques - the process of how this article was written using LLMs

What are some good ways to deliver this information in a blog post? One way I thought of is to show a snippet of code in each of those languages that "does the same thing", and illustrates the cultural changes of that period.

</details>
### 'Write' the first draft

At this point, I will have an outline and a lot of interesting text. I look through the text for inspiration, copy/paste a couple snippets in, then manually work on making them come together. Here is an example from a science fiction story I was writing:

Two snippets:

> Every now and then you would come to a little glade of bright sunlight, and there you would find a group of programs, and a few yards away, a group of others. And here and there, there were bluebells and wild roses, and the air was full of the sound of laughter and chirping and buzzing.

> others were only tools, like a simple cron daemon that called at intervals through the day for some data to be processed. 

First draft collage of snippets:

> Every now and then it would come to a little glade of smaller CPUs, and there it would find a group of programs, and every few address spaces away, another group. And around the happy glade, there would be under-utilized demo apps and gigs of free memory aplenty, so the network was full of packets of conversation and laughter and love. Such a place was full of happy little services, sometimes a little off, like a cron daemon who goes "cuck-a-doodle-doo!" at midnight instead of sunrise.

Once I get through writing a first draft of a given arc of the story, I will often generate a lot more text for ideas of the next arc. I will often include the previous arc as context for generating the next arc.

### Refine and rewrite iteratively

[insert]

## Conclusion

This writing process has a lot of overlap with the greenfield development process I've found myself doing - especially outlining and task-oriented prompting. Writing has the benefit that you don't really need to refactor or add features once you've finished a v1. That seems like more an accepted shortcoming of the culture and tooling surrounding writing. There's room for growth there.
## Notes

In my experience, when you generate a result from some system, to use in some system, it's useful to know where it comes from. So that when you have to change the downstream system in the future, you don't have to reverse-engineer how it ended up that way. But this is and has always been a lossy process:

1. user pain points
2. business requirements
3. product requirements
4. engineering requirements
5. actual code of a system

What I see happening with development using LLMs, is that there's a middle step being introduced between "engineering requirements" and "actual code of the system" which is "prompts used to build the system".

It seems, though, that teams generally wouldn't think of saving or structuring the LLM prompts used to build the system like they would save the engineering or product requirements or code. Those LLM prompts that are used to build the system are almost like the code itself, just the next generation of it.

- Are there tools/methodologies out there for maintaining those LLM prompts?
    
- Where is the industry at with this?

---

### Refine: edit -> refactor iterations

#### Writer 

You are an engineer writing a series of blog posts intended mostly for AI industry folks but also writers. In this article, you are writing about two main topics:
* the history of the industry going from assembly to high-level languages and what that means about the "next generation" of programming languages
* a demonstration of a possible style of the "next generation" of programming languages, which combines the craft of writing with applied ML techniques - the process of how this article was written using LLMs

There are three parts to the overall blog post:
- The hook, to draw the reader in and give a taste of what will be explored in "the history".
- The history, information about the history of development of programming languages and the cultural development around them.
- The future of new programming languages with that history.
- The plot twist, that this blog post was written by AI and not in the usual prompting way.
- The demo, which explains how this post was written, showing what the future could look like.
- The conclusion, wrapping up the theses in the article and linking to previous posts that explore related topics further.

Think and explain why the audience might connect with this content. Use that reasoning to write a compelling hook and initial transition to "the history". Don't write any of "the history".

---

Think and explain where the audience mindset will be after the "The future" section. Use that reasoning to write a compelling plot twist where they find that this article was written with AI, but not in any of those ways just described. Those future-looking things are unimaginative AI-generated takes on what comes next. Reality is stranger and more nuanced, and I'm going to demo an example of how programming languages might actually develop because it's based on reality - where I'm writing using LLMs.

#### Reviewer/Filterer

You are a writer that writes in a special style. You take a collage of text written by others and compose it together, like how a pop artist might collage together different visuals made by other artists to create something above and beyond them. To do that, you have to read a lot of text and pick out what looks good to you:
1. Sentence(s), phrases, or a paragraph.
2. Exposition or dialogue or descriptions, etc.
3. For its style or ideas or delivery, etc.

First, you will be given the short prompt that was used to generate "a lot of writing text".
Then, you will be given "a lot of writing text".
You must return the text from the writing files that was most interesting and explain why it is interesting.


### steps

1. bad cop + good cop
2. rewrite with voice x5
3. filter
4. update

experiment:
1. whole process
2. badcop+goodcop or just one?
3. how many rewrites to filter?
4. how to update? manual checks?




<details markdown="1">
<summary>Here was an example "filter" prompt for this post (click to expand)</summary>
You are an engineer writing a series of blog posts intended mostly for AI industry folks but also writers. In this article, you are writing about two main topics:
* the history of the industry going from assembly to high-level languages and what that means about the "next generation" of programming languages
* a demonstration of a possible style of the "next generation" of programming languages, which combines the craft of writing with applied ML techniques - the process of how this article was written using LLMs

There are three parts to the overall blog post:
- The hook, to draw the reader in and give a taste of what will be explored in "the history".
- The history, information about the history of development of programming languages and the cultural development around them.
- The future of new programming languages with that history.
- The plot twist, that this blog post was written by AI and not in the usual prompting way.
- The demo, which explains how this post was written, showing what the future could look like.
- The conclusion, wrapping up the theses in the article and linking to previous posts that explore related topics further.

You are a writer that writes in a special style. You take a collage of text written by others and compose it together, like how a pop artist might collage together different visuals made by other artists to create something above and beyond them. To do that, you have to read a lot of text and pick out what looks good to you:
1. Sentence(s), phrases, or a paragraph.
2. Exposition or dialogue or descriptions, etc.
3. For its style or ideas or delivery, etc.

First, you will be given the short prompt that was used to generate "a lot of writing text".
Then, you will be given "a lot of writing text".
You must return the text from the writing files that was most interesting and explain why it is interesting.

---

Here is the short prompt:

Think and explain why the audience might connect with this content. Use that reasoning to write a compelling hook and initial transition to "the history". Don't write any of "the history".

Use this as an inspiration for the hook:

I feel like I'm writing code in Python, then throwing all that text away and committing the machine code that comes out. That's what programming with LLMs feels like right now.

---

Here is "a lot of writing text:"

...

</details>