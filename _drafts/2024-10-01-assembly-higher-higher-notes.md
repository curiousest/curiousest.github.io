---
layout: post
title: Assembly to high-level languages - what did that look like?
date: 2024-09-01T00:00:00.001-05:00
author: Douglas Hindson
tags:
  - projects
modified_time: 2024-09-01T00:00:00.001-05:00
---

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

## Prompts

### Research

https://chatgpt.com/share/66f025ec-24c4-800f-9c34-3866f089fd48

You are an academic historian of computation with expertise in the history and development of computing technology. I am an engineer seeking a deep understanding of this field. As we engage in this discussion, please provide well-reasoned, detailed, and accurate responses, citing reputable sources whenever possible. If any assumptions or uncertainties arise, make them explicit, and clearly distinguish between verified information and speculation. Prioritize clarity, precision, and evidence-based reasoning in your explanations, and ensure that you provide context when introducing historical events, concepts, or figures.

I am writing a post about a brief history of the transition from low-level programming to where we are today. I want to use that history to illustrate what may happen in the future with LLMs. What are considered to be the main events in the transition from low-level languages to high-level languages? I'm interested both in technological achievements and cultural developments in the computing/high-tech industry.

What indicators suggest or detract from the possibility that we are now transitioning to a next generation of higher-level programming languages?

What technological advancements and cultural phenomena could happen again, but now with the next generation of languages?

### Outlining

I did this part manually.

### Initialize content

https://chatgpt.com/share/66f02ecb-7d54-800f-b6a9-54d8e5db069d

You are an engineer writing a series of blog posts intended for AI industry folks and writers. In this article, you are writing about two main topics:
* the history of the industry going from assembly to high-level languages and what that means about the "next generation" of programming languages
* a demonstration of a possible style of the "next generation" of programming languages, which combines the craft of writing with applied ML techniques - the process of how this article was written using LLMs

What are some good ways to deliver this information in a blog post? One way I thought of is to show a snippet of code in each of those languages that "does the same thing", and illustrates the cultural changes of that period.

---

### 1. **Early Assembly Language (1940s-1950s)**
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
   - **Code-culture commentary:** This snippet shows how early assembly languages required intimate knowledge of hardware instructions, making programming highly specialized.

### 2. **The Birth of High-Level Languages (1950s)**
   - **FORTRAN (1957)**: The first widely used high-level programming language, FORTRAN (FORmula TRANslation), was developed by IBM, specifically for scientific and engineering calculations. It abstracted away many hardware-specific details, allowing more focus on problem-solving.
   - **COBOL (1959)**: Developed for business applications, COBOL (Common Business-Oriented Language) emphasized readability and was designed for data processing. It marked a shift towards programming languages that non-engineers could learn.
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

### 3. **Standardization and Compiler Advances (1960s-1970s)**
   - **ALGOL (1960)**: Introduced concepts like structured programming and recursion, influencing future languages like C and Pascal. ALGOL is often considered a pivotal step in defining what high-level languages could be.
   - **The Development of C (1972)**: Created by Dennis Ritchie at Bell Labs, C struck a balance between high-level abstraction and low-level access to hardware. Its portability, power, and efficiency made it foundational for system software, including operating systems like UNIX.
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

### 4. **The Advent of Object-Oriented Programming (OOP) (1970s-1980s)**
   - **Smalltalk (1972) and C++ (1983)**: Smalltalk pioneered the concept of object-oriented programming, while C++ brought OOP concepts into the mainstream by building on C. This shift allowed programmers to model real-world problems more intuitively and led to more manageable, reusable, and scalable code.
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
### 5. **The Rise of Scripting and Interpreted Languages (1990s)**
   - **Languages like Python (1991), Perl (1987), and JavaScript (1995)** became popular for their ease of use and flexibility. They allowed rapid prototyping and development, especially for web applications.
   - **Java (1995)**: Promised "write once, run anywhere," contributing to a surge in cross-platform development. This reinforced the idea that programming should focus on solving problems, not worrying about hardware specifics.
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
### 6. **The Dominance of Frameworks and Libraries (2000s)**
   - The 2000s brought about an explosion of frameworks (e.g., Ruby on Rails, Django, .NET) and libraries that abstracted away even more complexity, allowing developers to build sophisticated applications with minimal code.
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
### 7. **The Age of Declarative and Functional Paradigms (2010s)**
   - **Rise of Functional Languages**: While functional programming existed since the 1950s (e.g., LISP), it gained renewed interest with languages like Haskell, Scala, and Elixir due to their ability to handle concurrency and parallelism efficiently.
   - **Declarative Programming**: Languages and frameworks that emphasize "what to do" instead of "how to do it," such as SQL, HTML, and modern web frameworks like React, gained popularity.
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

---

### **1. Evolution of Abstraction Layers**

#### **What Happened Before**:

The shift from assembly language to high-level languages like FORTRAN and COBOL marked a dramatic increase in abstraction. This evolution allowed developers to focus more on problem-solving and less on hardware-specific details.

#### **What Could Happen Again: Natural Language Programming & Intent-Based Programming**

- **Natural Language Programming**: Just as early high-level languages made it easier for engineers to express complex logic, the next generation of languages could harness natural language more effectively, allowing developers to describe software behavior in plain human language. Tools like OpenAI's Codex and GitHub Copilot are precursors, but we might see integrated development environments (IDEs) where programming and documentation merge seamlessly, reducing the distinction between code and natural language instructions.
  
- **Intent-Based Programming**: Moving from "how" to "what," we could see languages that allow developers to define end goals, with the system handling the specifics. This approach would echo the rise of declarative programming but at a much more sophisticated level, where intent and constraints become the primary means of interaction.

##### **Future LLM-Oriented Approach:**

[insert example of a collection of prompts that collectively define a product]


**Commentary:** Here, the developer only needs to specify the goal ("calculate the factorial"), and the system automatically handles the translation into executable code. This echoes the abstraction seen in early high-level languages but at a much more sophisticated level.

---

### **2. Growth of Domain-Specific Languages (DSLs)**

#### **What Happened Before**:

DSLs like SQL, HTML, and CSS emerged to address specific problem domains, allowing users to interact with computers in more intuitive, task-oriented ways.

#### **What Could Happen Again: AI-Augmented DSLs & Multi-Modal DSLs**

- **AI-Augmented DSLs**: The next generation might involve AI-powered DSLs tailored to niche domains, such as finance, healthcare, or manufacturing. These languages could dynamically adapt based on user input, learning from domain experts and incorporating industry-specific terminology and practices in real-time.
  
- **Multi-Modal DSLs**: Just as DSLs allowed programmers to specialize, we might see DSLs that blend different media (text, voice, images) for more intuitive problem-solving. For instance, a data analyst could draw a diagram and annotate it with natural language, with the system converting this input into a structured, executable data transformation pipeline.

##### **Future AI-Augmented DSL Approach:**

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

**Commentary:** 

---

### **3. Standardization and Emergence of Shared Protocols**

#### **What Happened Before**:

The creation of standardized languages and protocols, such as ANSI C, POSIX, and the ISO standards for languages like SQL, helped unify the computing industry, allowing code to be more portable and interoperable.

#### **What Could Happen Again: Interoperability Standards for AI-Driven Development**

- **Interoperability Standards for AI-Driven Development**: As AI-assisted coding becomes more prevalent, we might see the emergence of standardized interfaces for LLMs, allowing different tools to communicate seamlessly. This development would parallel the standardization seen with programming languages, but applied to AI models, data formats, and intent representations.
  
- **Cross-Platform Natural Language APIs**: Similar to how languages like Java provided a "write once, run anywhere" experience, we could see frameworks where instructions given in natural language are converted into executable code across multiple platforms, allowing non-programmers to interact with different systems without worrying about underlying languages or frameworks.

##### **Future Approach: Cross-Platform Natural Language APIs**

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

**Commentary:** This JSON-based format could be understood and executed across different platforms and languages, allowing both humans and AI agents to read and execute the instructions seamlessly.

---

### **4. Democratization of Programming**

#### **What Happened Before**:

The advent of BASIC in the 1960s and the personal computer revolution of the 1980s empowered hobbyists and non-experts to write programs. This democratization led to a surge in creative, diverse software development and a wave of technological innovation.

#### **What Could Happen Again: Citizen Development Powered by AI**

- **Citizen Development Powered by AI**: Just as BASIC empowered home computer enthusiasts, AI-driven low-code/no-code platforms could enable a new generation of "citizen developers." These tools could become sophisticated enough that individuals without formal programming training could build complex, domain-specific applications, potentially leading to another wave of grassroots innovation.
  
- **Global, Inclusive Programming Communities**: The barrier to entry might drop so low that communities from regions currently underrepresented in software development become major contributors, fostering a more diverse ecosystem of creators. Imagine forums or collaborative platforms where people from different disciplines, speaking different languages, contribute ideas that are instantly translatable into executable code.

##### **Future Low-Code/No-Code Platform Approach:**

Imagine a voice no-code environment:

```
Make a calculator app with the factorial function and install it on my phone.
Make a short video course to explain why it might be important to me and how it works.
```

**Commentary:** This example illustrates how AI-driven platforms could allow anyone, regardless of technical background, to build and execute complex logic using natural language.

---

### **5. Cultural Shifts Toward Collaboration and Open Source**

#### **What Happened Before**:

The rise of UNIX, Linux, and the open-source movement in the late 20th century created a culture of sharing, collaboration, and collective problem-solving. This ethos was fundamental to the success of technologies like the World Wide Web.

#### **What Could Happen Again: Community-Driven Language Evolution**

- **Open-Source AI Models and Knowledge Bases**: As LLMs and AI-driven tools become more integrated into programming, open-source AI models might become the norm, leading to a collaborative culture around improving these systems. We could see shared repositories of "intent patterns" or common knowledge structures that help AI tools better understand and respond to different problem domains.
  
- **Community-Driven Language Evolution**: Just as the open-source community contributes to language development (e.g., Python's PEP process), the next generation might involve real-time, collaborative evolution of AI-driven languages, with users contributing refinements to how the system understands and responds to natural language input.

##### **Future Open-Source LLM Code Repository Approach:**

Developers collaborate on an open-source LLM "snippet" repository, where they define common functions like factorials. You might pull the latest community-optimized version:

```python
# Fetch and execute the latest community version of the factorial function
factorial = get_open_source_function("factorial", "v1.2.3")
result = factorial(5)
```

**Commentary:** The factorial function isn’t just defined by one person—it’s the product of collective knowledge, continuously refined and improved by the community, allowing you to pull and use the best version available.

---

### **6. The Emergence of New Programming Paradigms**

#### **What Happened Before**:

The shift to object-oriented programming (OOP) in the 1980s and the later rise of functional programming introduced new ways of thinking about software design, allowing developers to model problems more effectively.

#### **What Could Happen Again: Contextual Programming & Collaborative, Multi-Agent Programming**

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

## Refine: edit -> refactor iterations

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

Use this as an inspiration for the hook:

I feel like I'm writing code in Python, then throwing all that text away and committing the machine code that comes out. That's what programming with LLMs feels like right now.

---

Think and explain where the audience mindset will be after the "The future" section. Use that reasoning to write a compelling plot twist where they find that this article was written with AI, but not in any of those ways just described. Those future-looking things are unimaginative AI-generated takes on what comes next. Reality is stranger and more nuanced, and I'm going to demo an example of how programming languages might actually develop because it's based on reality - where I'm writing using LLMs.

> “The Matrix is surely the kind of film about the matrix that the matrix would have been able to produce.”
> “The actors are in the matrix, that is, in the digitized system of things; or, they are radically outside it, such as in Zion, the city of resistors. But what would be interesting is to show what happens when these two worlds collide. The most embarrassing part of the film is that the new problem posed by simulation is confused with its [classical, Platonic treatment](https://baudrillardstudies.ubishops.ca/the-matrix-decoded-le-nouvel-observateur-interview-with-jean-baudrillard/#:~:text=The%20actors%20are,classical%2C%20Platonic%20treatment).”
-Jean Baudrillard, 2004