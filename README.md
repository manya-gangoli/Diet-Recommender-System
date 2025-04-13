
<h1>Recipe Recommendation System</h1>

<h2>Introduction</h2>
<p>This project implements a data-driven recipe recommendation system that suggests recipes based on user nutritional preferences. The system leverages a comprehensive dataset of 7,610 recipes across five diet types (paleo, vegan, keto, mediterranean, and dash) and 19 cuisine types. By utilizing similarity metrics, the system can match user nutritional requirements with appropriate recipes, while also accommodating preferences for specific ingredients, diet restrictions, or cuisine preferences.</p>


<h2>Project Goal</h2>
    <p>The primary objective of this project is to create a personalized recipe recommendation engine that:</p>
 <ul>
        <li>Helps users discover recipes matching their specific nutritional needs</li>
        <li> Accommodates dietary preferences and restrictions</li>
        <li>Suggests recipes with similar nutritional profiles to user requirements</li>
    </ul>

    
 <h2>Methodology</h2>
    <ol>
        <li><strong>Data Preparation:</strong> 
            <ul>
                <li>Exploratory Data Analysis to understand the distribution of diet types and cuisine types.</li>
                <li>Data cleaning to remove duplicates and ensure data integrity.</li>
                <li>Feature engineering to normalize nutritional values using Min-Max scaling</li>
            </ul>
        </li>
        <li><strong>Recommendation Algorithm:</strong> 
            <ul>
                <li>Normalization of user input (protein, carbs, fat) to match dataset scaling</li>
                <li>Application of user-specified filters (ingredient, diet type, cuisine type)</li>
              <li>Calculation of cosine similarity between user preferences and recipe nutritional profiles</li>
               <li>Ranking and returning top recipe matches as recommendations</li>
            </ul>
        </li>
    </ol>




  <h2>Future Scope</h2>
        <ul>
        <li><strong>Enhanced Nutritional Matching:</strong>Incorporate additional nutritional parameters (calories, vitamins, minerals)</li>
        <li><strong>Meal Planning:</strong> Add functionality to create full meal plans based on daily nutritional targets</li>
        <li><strong>Feedback Mechanism: </strong>  Implement user feedback and rating system to improve recommendations over time.</li>
    </ul>
    

<h2>Contributor</h2>
    <ul>
        <li><strong>Manya Gangoli</strong></li>
    </ul>

 <h2>Contact Information</h2>
    <p>For inquiries or collaboration, feel free to reach out:</p>
    <ul>
        <li>Email: <a href="mailto:manyagangoli14@gmail.com">manyagangoli14@gmail.com</a></li>
         <li>LinkedIn: <a href="https://www.linkedin.com/in/manyagangoli/">Manya Gangoli</a></li>
 </ul>

</body>
</html>
