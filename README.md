# Lost and Found Platform

## Introduction

Lost and Found Platform is a web application designed to reunite users with their lost belongings. Whether it's a misplaced wallet at a crowded event or a forgotten item during day-to-day activities, Lost and Found provides a centralized hub for reporting lost items and facilitating their recovery.

- **Deployed Site:** [Lost and Found Platform]([https://www.lostandfound.com](https://mugishagoal.github.io/Lost_and_found_platform/))
- **Landing page:**  [Lost and Found Platform].(https://mugishagoal.github.io/Landing_page_L-F/).
- **Final Project Blog Article:** [Lost and Found: Bridging the Gap Between Lost Items and Their Owners]([https://www.lostandfound.com/blo](https://www.linkedin.com/posts/mugisha-benjamin-de-gaulle-bab991249_introducing-our-lost-and-found-platform-lost-activity-7166142648393707521-rqUK?utm_source=share&utm_medium=member_desktop)
- **Author(s) LinkedIn:** [MUGISHA Benjamin De Gaulle](https://www.linkedin.com/in/mugisha-benjamin-de-gaulle-bab991249)

## Installation

To install Lost and Found Platform locally, follow these steps:

1. Clone the repository: `git clone [https://github.com/yourusername/lost-and-found.git](https://github.com/MugishaGoal/Lost_and_found_platform)`
2. Navigate to the project directory: `cd lost-and-found_platform`
3. Install dependencies: `pip install``

## Usage

To use Lost and Found Platform:

1. Start the development server: `npm start` or `yarn start`
2. Open your web browser and navigate to `http://localhost:3000`

## Contributing

We welcome contributions from the community! If you'd like to contribute to Lost and Found Platform, please follow these guidelines:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Make your changes and commit them: `git commit -m 'Add your feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Submit a pull request

## Related Projects

Check out these related projects:

- [FoundIt: Mobile App for Lost and Found](https://github.com/username/foundit)
- [Lost and Found API: Backend for Lost and Found Platform](https://github.com/username/lost-and-found-api)

## Licensing

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.




 

Lost and Found Platform
Connecting people with their lost items and fostering a community-driven approach to reuniting valuables through a centralized and user-friendly platform.

─
<TEAM>
Team Member: Mugisha Benjamin De Gaulle
Role: Project Manager and Full Stack Developer
Reasoning:
The chosen role of Project Manager and Full Stack Developer is based on the understanding that a single individual will be responsible for overseeing the entire project lifecycle, from conceptualization to implementation. This streamlined approach ensures quick decision-making, efficient communication, and a seamless integration of both the front-end and back-end components of the Lost and Found Platform. This role combines leadership and technical skills, allowing for a comprehensive and cohesive development process.


<TECHNOLOGIES>

Programming Languages:
Chosen: Python (Flask for backend) and JavaScript (React & JQuery for frontend)
Alternative: Django for backend and Angular for frontend
Trade-offs: While Django is a high-level Python web framework that follows the Model-View-Controller (MVC) pattern, Flask is a micro-framework providing flexibility. React is a popular JavaScript library for building user interfaces, and Angular is a more comprehensive JavaScript framework.
Decision: I chose Flask and React &JQuery for their simplicity, flexibility, and ease of integration. Flask allows more control over components, and React's virtual DOM enhances performance.
Database:
Chosen: MySQL
Alternative: PostgreSQL
Trade-offs: PostgreSQL is known for advanced features, extensibility, and support for complex queries. MySQL is widely used, has good performance, and is well-supported.
Decision: I chose MySQL for its familiarity, community support, and suitability for the scale of the Lost and Found Platform.
Backend Framework:
Chosen: Flask (Python)
Alternative: Django (Python)
Trade-offs: Django is a high-level framework with built-in features, but Flask offers simplicity and customization.
Decision: I chose Flask for its lightweight nature, allowing more control over components and a minimalist approach for a focused Lost and Found Platform.
Frontend Library/Framework:
Chosen: React & JQuery(JavaScript)
Alternative: Angular (JavaScript)
Trade-offs: Angular is a full-fledged framework with more features, while React is a library providing more flexibility.
Decision: I chose React and Jquery for their component-based architecture, virtual DOM, and a vibrant community, aligning with the project's requirements.
Version Control:
Chosen: Git
Alternative: Mercurial
Trade-offs: Git is more widely adopted, has a larger community, and is the industry standard. Mercurial is simpler and may be preferable for certain workflows.
Decision: I chose Git due to its ubiquity, strong branching model, and extensive ecosystem.
Containerization:
Chosen: Docker
Alternative: Podman
Trade-offs: Docker is the industry standard with broad support. Podman is daemonless and more suited for certain security contexts.
Decision: I chose Docker for its widespread adoption, community support, and seamless integration with other tools.
Deployment:
Chosen: Heroku
Alternative: AWS Elastic Beanstalk
Trade-offs: Heroku is easy to use, while AWS Elastic Beanstalk offers more control over infrastructure.
Decision: Chose Heroku for its simplicity, quick deployment, and suitable features for the initial project phase.
Authentication:
Chosen: OAuth2
Alternative: JWT (JSON Web Tokens)
Trade-offs: OAuth2 is an industry standard for authentication, while JWT is simpler and suitable for certain use cases.
Decision: I chose OAuth2 for its widespread adoption, delegated authorization, and secure authentication flow.
Real-time Communication:
Chosen: Socket.IO
Alternative: WebSocket API
Trade-offs: Socket.IO is a library providing real-time bidirectional event-based communication, while WebSocket API is a lower-level protocol.
Decision: I chose Socket.IO for its ease of use, fallback mechanisms, and support for various transport protocols.
Development Environment:
Chosen: Visual Studio Code
Alternative: PyCharm
Trade-offs: Visual Studio Code is lightweight and versatile, while PyCharm is a dedicated Python IDE with advanced features.
Decision: I chose Visual Studio Code for its broad language support, extensions, and community plugins.
These technology choices were made based on a balance between project requirements, development team expertise, community support, scalability, and ease of integration. The final decision aimed to provide a robust and efficient Lost and Found Platform while ensuring maintainability and extensibility.

<CHALLENGE>

Problem Statement:
Description: The Lost and Found Platform addresses the common challenge of losing personal belongings in public spaces or events, providing a centralized system for reporting and locating lost items.
Problem to Solve: The inconvenience and stress caused by losing valuable possessions in public areas where individuals may not have direct means of communication.
Limitations - What the Project Will Not Solve:
Scope: The Lost and Found Platform is not designed to handle cases of theft or deliberate misplacement. It focuses solely on facilitating the recovery of items that have been unintentionally lost.
Target Users and Beneficiaries:
Users:
General Public: Individuals who have lost personal items and those who find lost items and wish to return them.
Event Organizers: To enhance attendee experience and provide a value-added service during events.
Beneficiaries:
Individuals: Regain lost belongings and experience a more efficient process for item retrieval.
Event Organizers: Improve attendee satisfaction and overall event experience.
Relevance to Locale:
The Lost and Found Platform is designed to be adaptable to various locales, including Rwanda. While the core functionality remains relevant globally, localized features may be integrated to enhance usability in specific regions.
In summary, the Lost and Found Platform aims to alleviate the stress of losing personal items in public spaces, offering a user-friendly interface for reporting lost items and facilitating their recovery. It provides benefits to both individuals who have lost belongings and those who find lost items, enhancing overall community well-being. The project's relevance to a specific locale can be achieved through thoughtful customization and adaptation to local needs.

<RISKS>

Database Scalability:
Potential Impact: As the platform grows, a traditional relational database might face scalability challenges, leading to performance issues.
Safeguard/Alternative: Implement a scalable database solution such as sharding or NoSQL databases. Regularly monitor database performance and consider cloud-based solutions.
Security Vulnerabilities:
Potential Impact: Security breaches could compromise user data and the integrity of the platform.
Safeguard/Alternative: Regular security audits, encryption of sensitive data, and adherence to security best practices. Employ penetration testing to identify and address vulnerabilities.
Real-time Communication Challenges:
Potential Impact: Issues with real-time features like notifications or updates may affect the user experience.
Safeguard/Alternative: Use reliable libraries or services for real-time communication, implement fallback mechanisms, and conduct thorough testing in various network conditions.
User Privacy Concerns:
Potential Impact: Users may be reluctant to use the platform if they have concerns about privacy and data protection.
Safeguard/Alternative: Clearly communicate the platform's privacy policy, implement robust data protection measures, and provide users with control over their data. Comply with relevant data protection regulations.
Non-Technical Risks:
Low User Adoption:
Potential Impact: If users do not adopt the platform, its effectiveness will be limited.
Strategy: Conduct user research, engage potential users in the development process, and implement a user-friendly interface. Promote the platform through marketing and partnerships.
Legal and Regulatory Compliance:
Potential Impact: Failure to comply with legal requirements and regulations may lead to legal issues.
Strategy: Stay informed about relevant laws and regulations, especially concerning lost and found items. Consult legal professionals to ensure compliance and address any legal concerns proactively.
Negative Public Perception:
Potential Impact: Negative publicity or perceptions about the platform's efficacy may hinder its success.
Strategy: Maintain transparency in communication, actively address user feedback, and continuously improve the platform based on user experiences. Implement a robust customer support system.
Event Organizer Resistance:
Potential Impact: Resistance from event organizers to integrate the platform into their events.
Strategy: Showcase the benefits of the platform to event organizers, emphasizing improved attendee experience, positive engagement, and the added value it brings to events.
By identifying and addressing these technical and non-technical risks proactively, the Lost and Found Platform can enhance its chances of success and sustainability in the long run. Regular monitoring, feedback loops, and adaptability will be key components of risk mitigation strategies.

<INFRASTRUCTURE>

No process of branching and merging because I’ll do it solely.
Continuous Integration/Continuous Deployment (CI/CD):
Utilize CI/CD pipelines to automate the deployment process.
Integrate version control (Git) with CI/CD tools to ensure a seamless and controlled deployment pipeline.
Choose a cloud platform (e.g., Heroku) for its ease of deployment and scalability.
Staging Environment:
Implement a staging environment for thorough testing before production deployment.
Conduct comprehensive testing, including unit tests, integration tests, and user acceptance tests, in the staging environment.
Rolling Deployment:
Implement a rolling deployment strategy to minimize downtime and ensure a smooth transition.
Use containerization (Docker) to encapsulate the application and manage dependencies consistently.
Monitoring and Rollback:
Implement robust monitoring tools to track the application's performance in real-time.
Set up automated alerts for any anomalies or errors.
Include a rollback plan in case unexpected issues arise during or after deployment.
Data Population:
Manual Seed Data:
Manually populate essential data during the initial setup, including user roles, initial configurations, and predefined categories.
User-Generated Data:
Encourage user participation to contribute to the lost and found database by reporting and claiming items.
Implement moderation features to ensure data quality and prevent misuse.
Integration with External Databases:
Explore partnerships with organizations or events that already manage lost and found data.
Establish APIs or data exchange mechanisms to integrate external data sources.
Testing Tools and Automation:
Unit Testing:
Use testing frameworks like Unitest for Python to conduct unit tests for individual components and functions.
Implement test-driven development (TDD) practices to ensure code reliability.
Integration Testing:
Employ tools such as Selenium for automated end-to-end testing of the web application.
Conduct integration tests to verify the interaction between different modules.
Load Testing:
Utilize tools like Locust or cloud-based services to simulate various user loads and assess the application's performance under stress.
Security Testing:
Conduct regular security audits using tools like OWASP ZAP to identify and address potential vulnerabilities.
Integrate security testing into the CI/CD pipeline for continuous security checks.
User Acceptance Testing (UAT):
Engage real users or stakeholders in UAT to ensure the application meets their expectations and requirements.
Collect feedback and address any usability issues identified during UAT.
Code Reviews:
Implement a code review process to ensure code quality, adherence to best practices, and knowledge sharing among team members.
By combining automated testing, manual testing, and a well-defined deployment strategy, the Lost and Found Platform can maintain a robust and reliable application throughout its lifecycle. Regular updates and improvements can be seamlessly integrated into the deployment pipeline while ensuring the platform's stability and security.

<EXISTING SOLUTIONS?

Tile:
Similarities:
Tile is a popular lost and found solution that helps users locate misplaced items using Bluetooth trackers.
Like the proposed Lost and Found Platform, Tile provides a way for users to report lost items and leverage a community network for locating them.
Both platforms aim to assist users in retrieving lost belongings through a technology-driven approach.
Differences:
Tile primarily relies on physical Bluetooth-enabled devices attached to items, whereas the Lost and Found Platform focuses on a digital platform accessible through web and mobile interfaces.
The proposed platform encourages community involvement by allowing users to report and claim lost items, fostering a collaborative environment not present in Tile's model.
LostMyDoggie:
Similarities:
LostMyDoggie is a service that helps individuals find lost pets by creating and distributing lost pet posters.
Like the Lost and Found Platform, LostMyDoggie aims to facilitate the reunification of lost items (pets in this case) with their owners through a digital platform.
Differences:
LostMyDoggie is specialized in finding lost pets, whereas the Lost and Found Platform is designed for a broader range of lost items.
The proposed platform integrates modern technologies such as real-time communication (Socket.IO) and a dynamic web interface, distinguishing it from LostMyDoggie's traditional poster-based approach.

While existing solutions like Tile and LostMyDoggie address specific niches within the lost and found domain, the proposed Lost and Found Platform differentiates itself by combining digital and community-driven elements, making it versatile and accessible to a wider audience.
THANKS!

