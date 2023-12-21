# Doormot
Doormot is a web application that connects people who need landed property to the right property for them.
This project started at exactly  November 4, 2023, at 18:46:04 (2023-11-04 18:46:04.576662000 +0100)

Property Connect Web Application
Overview

Welcome to Property Connect, a web application designed to connect individuals with their ideal landed properties. This comprehensive README provides detailed insights into the project, its architecture, technologies used, development journey, lessons learned, and future steps. The app aims to streamline the process of finding suitable landed properties for users.
Table of Contents

    Project Overview
    Architecture and Technologies
    Development Journey
        Successes
        Challenges
        Areas for Improvement
    Lessons Learned
    Next Steps
    Conclusion
    GitHub Repository
    Installation
    Usage
    Contributing
    License

Project Overview

Property Connect is a web application created to facilitate the seamless connection of individuals with their desired landed properties. Due to unforeseen circumstances, the project is currently a solo endeavor. The app is intended to simplify the property search process for users.
Architecture and Technologies
Technical Breakdown

The application is built using the following technologies:

    Django (Python 37%)
    JavaScript (17.7%)
    Tailwind CSS (19.3%)
    HTML (26%)

Architectural Decisions
Custom Authentication

Faced challenges with users appearing as anonymous after authentication, resolved by passing the authenticated user to the context.
Product Uploads

Overcame challenges connecting user types and product uploads using generic foreign keys and reverse relation links.
User Models

Opted for individual models for each user type, avoiding simultaneous authentication issues.
Development Journey
Successes

    Seamless authentication was achieved after overcoming initial hurdles.
    Successful implementation of generic foreign keys for flexible product uploads.

Challenges

    Initial struggles with custom login authentication.
    Establishing connections between user types and product uploads.
    Creating distinct models for different user types to avoid authentication conflicts.

Areas for Improvement

    Continuous refinement of the product upload process.
    Enhancements to custom login authentication for a smoother user experience.

Lessons Learned

    System Comprehension is Key:
        Emphasizes the importance of understanding the system and architecture in development.
    Adaptability and Iteration:
        Acknowledges the significance of adaptability and continuous iteration in overcoming challenges.

Next Steps

    Continuous refinement and fine-tuning of the project.
    Ongoing work to enhance the user experience and address any unforeseen challenges.

Conclusion

The Property Connect web application has been a journey marked by both challenges and rewards. The experience underscores the critical role of system comprehension in development. The project looks forward to further evolution and refinement.
GitHub Repository

[[Link to GitHub:https://github.com/Poltergeist1717/Doormot/edit/main/README.md]
Installation

To install and run the application locally, follow these steps:

    Clone the repository.
    Navigate to the project directory.
    Install dependencies using pip install -r requirements.txt.
    ...

Usage

Provide detailed instructions on how to use the application, including any specific configurations or settings.
Contributing

I've learned a lot from various sources, including ChatGPT, Google, Stack Overflow, and the valuable contributions of some colleagues. Contributions to the project are welcome. If you're interested in contributing, please follow the guidelines outlined in the Contributing file.
License

The project is not yet distributed, and I haven't decided on the license. Please stay tuned for updates on the project's licensing.
