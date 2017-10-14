from bs4 import BeautifulSoup

siteHTML = """
<ul class="browse-product-cards clearfix major category">
 <li class="index-2-0 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/123d-circuits" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="123D Circuits" class="" src="https://edsurge.imgix.net/uploads/product/image/1578/g_zF9_lf_400x400-1429138239.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      123D Circuits
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Online circuit simulator
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 44 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/accelerated-reader" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-star" title="Product Brief Available">
     <div class="browse-product-card-star-text">
      ★
     </div>
    </div>
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Accelerated Reader 360" class="" src="https://edsurge.imgix.net/uploads/product/image/18/AR_360-1440527168.jpeg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Accelerated Reader 360
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Reading comprehension program that monitors, manages and tests elementary students
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/act-career-curriculum" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-star" title="Product Brief Available">
     <div class="browse-product-card-star-text">
      ★
     </div>
    </div>
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="ACT Career Curriculum" class="" src="https://edsurge.imgix.net/uploads/product/image/1373/act-1404841288-1412810270-1428744686-1428752472.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      ACT Career Curriculum
     </div>
     <div class="roboto browse-description-threelines grey-4">
      LMS and courses focused on building foundational workplace skills for adults
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/ardusat" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Ardusat" class="" src="https://edsurge.imgix.net/uploads/product/image/1551/Screen_Shot_2015-03-18_at_9.19.02_AM-1426695584-1428744966-1428752676.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Ardusat
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Hands-on STEM activities
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 13 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/artifact" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Artifact" class="" src="https://edsurge.imgix.net/uploads/product/image/1291/Artifact-1410237418-1428744513-1428752297.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Artifact
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Helps teachers, schools and libraries assign appropriate books based on student's reading level, standards, topics, etc.
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 36 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/bankaroo" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="bankaroo" class="" src="https://edsurge.imgix.net/uploads/product/image/1773/bankaroo-1448404616.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      bankaroo
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Learn financial literacy and basic banking transactions
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 42 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/beeline-reader" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="BeeLine Reader" class="" src="https://edsurge.imgix.net/uploads/product/image/1774/colored-1448404938.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      BeeLine Reader
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Facilitates on-screen reading using color gradients
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span>
      ･ 52 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/birdbrain-science" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="BirdBrain Science" class="" src="https://edsurge.imgix.net/uploads/product/image/946/bird-1455651297.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      BirdBrain Science
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Leveled, adaptive CCSS-based science articles for reading comp &amp; subject-specific vocab
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 234 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/booktrack-classroom-product" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Booktrack Classroom" class="" src="https://edsurge.imgix.net/uploads/product/image/1717/Screen_Shot_2015-1441336295.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Booktrack Classroom
     </div>
     <div class="roboto browse-description-threelines grey-4">
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 60 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/brainpop" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-star" title="Product Brief Available">
     <div class="browse-product-card-star-text">
      ★
     </div>
    </div>
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="BrainPOP" class="" src="https://edsurge.imgix.net/uploads/product/image/51/Brainpop_logo-01-1430260576.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      BrainPOP
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Animated movies, learning games, quizzes and interactive activities covering K-8 and ESL curriculum
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span>
      ･ 430 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/callido" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Callido Learning" class="" src="https://edsurge.imgix.net/uploads/product/image/1674/DvhIiF5K_400x400-1438208958.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Callido Learning
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Courses to develop research, information literacy and other critical thinking skills
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 14 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/canfigureit-geometry" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="CanFigureIt Geometry" class="" src="https://edsurge.imgix.net/uploads/product/image/1781/logo_CFI_Mar2016-1484588059.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      CanFigureIt Geometry
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Interactive geometry-learning program
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 36 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/cashtivity" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Cashtivity" class="" src="https://edsurge.imgix.net/uploads/product/image/760/Cashtivity_Logo_500-1493074103.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Cashtivity
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Project-based entrepreneurship, financial and business challenges
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 103 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/choosito" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Choosito" class="" src="https://edsurge.imgix.net/uploads/product/image/929/Choosito-1428743895-1428751808.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Choosito
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Optimized internet search tool that curates content based on subject and quality and matches it to students' reading levels
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 61 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/cicero-kids" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="CICERO Kids" class="" src="https://edsurge.imgix.net/uploads/product/image/1523/Slide1-1423519370-1428744900-1428752636.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      CICERO Kids
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Digital social studies resources in interactive museum setting
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 44 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/citelighter" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Citelighter" class="" src="https://edsurge.imgix.net/uploads/product/image/335/Citelighter2-1428742983-1428751005.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Citelighter
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Helps teachers streamline CCSS-aligned writing assignments, grading and measuring student performance
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 105 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/classk12" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="ClassK12" class="" src="https://edsurge.imgix.net/uploads/product/image/1935/19s0mJ03_400x400-1457723747.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      ClassK12
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Math &amp; ELA interactive work for young students
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 13 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/classroom-inc" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="After the Storm" class="" src="https://edsurge.imgix.net/uploads/product/image/447/AftertheStorm_HIGH_RES-1440623106.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      After the Storm
     </div>
     <div class="roboto browse-description-threelines grey-4">
      CCSS-aligned reading game and corresponding curriculum for Middle School students
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 100 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/codehs" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="CodeHS" class="" src="https://edsurge.imgix.net/uploads/product/image/318/93ab7351c9a6611b0a4be10a3c847dfd_400x400-1453507793.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      CodeHS
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Curriculum, teacher tools and teacher training to teach coding to high schoolers
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 24 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/codemonkey" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="CodeMonkey" class="" src="https://edsurge.imgix.net/uploads/product/image/1002/3tBsndTq_400x400-1486166460.jpeg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      CodeMonkey
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Online game that teaches computer programming to kids
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 16 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/code-red-education-product" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Code Red Education Coding Curriculum" class="" src="https://edsurge.imgix.net/uploads/product/image/1211/Code_Red_Education-1407962757-1428744388-1428752202.JPG?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Code Red Education Coding Curriculum
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Offers complete coding curriculum for K-12 students
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 16 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Core Curriculum
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/codesters" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Codesters" class="" src="https://edsurge.imgix.net/uploads/product/image/1796/pBdghHl5_400x400-1449697647.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Codesters
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Learning coding &amp; integrate into core subjects
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 45 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/collisions" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Collisions" class="" src="https://edsurge.imgix.net/uploads/product/image/1858/Collisions_icon_512_v03-1470687588.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Collisions
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Digital game for high school chemistry
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 31 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/commonlit" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="CommonLit" class="" src="https://edsurge.imgix.net/uploads/product/image/1579/CommonLit_New_Logo_Trans_Blue-1470714425.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      CommonLit
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Repository of free English texts, organized by theme
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span>
      ･ 24 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/compasslearning-odyssey" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-star" title="Product Brief Available">
     <div class="browse-product-card-star-text">
      ★
     </div>
    </div>
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="CompassLearning Odyssey" class="" src="https://edsurge.imgix.net/uploads/product/image/19/compasslearningodyssey-1428742437-1428750587.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      CompassLearning Odyssey
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Adaptive and assignable digital curriculum for most subjects K-12
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/comprendio" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Comprendio" class="" src="https://edsurge.imgix.net/uploads/product/image/2319/6A_2pVc5_400x400-1472852481.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Comprendio
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Organize STEM lessons; track student progress &amp;amp; understanding
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 10 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/conceptua-math" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Conceptua Math" class="" src="https://edsurge.imgix.net/uploads/product/image/737/regular_conceptuamath-1428743576-1428751537.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Conceptua Math
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Curriculum for Grades 3-5 math that includes multiple visual models, daily discussion, and assessments.
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 35 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Core Curriculum
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/core-skills-mastery" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-star" title="Product Brief Available">
     <div class="browse-product-card-star-text">
      ★
     </div>
    </div>
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Core Skills Mastery" class="" src="https://edsurge.imgix.net/uploads/product/image/539/CSMlogoMed-1428743307-1428751268.gif?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Core Skills Mastery
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Adaptive course prepares students for life, emphasizing problem solving persistence and more
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/cs-first" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="CS First" class="" src="https://edsurge.imgix.net/uploads/product/image/1729/Screen_Shot_2015-1443752484.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      CS First
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Free program that increases student access and exposure to computer science (CS) education through after-school, in-school, and summer programs
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 15 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/cuethink-product" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="CueThink" class="" src="https://edsurge.imgix.net/uploads/product/image/1160/CueThink-1406934835-1428744297-1428752108.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      CueThink
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Peer-to-peer mobile learning platform for students to improve their math problem solving skills
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 20 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/curriculet" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Curriculet" class="" src="https://edsurge.imgix.net/uploads/product/image/545/curriculet_logo_c_square_master_300px_white-1442418340.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Curriculet
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Manages reading assignments, allowing teachers to integrate media &amp; quizzes into ebooks
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 241 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Core Curriculum
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/dreambox-learning" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-star" title="Product Brief Available">
     <div class="browse-product-card-star-text">
      ★
     </div>
    </div>
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="DreamBox Learning" class="" src="https://edsurge.imgix.net/uploads/product/image/13/dreambox-1488389555.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      DreamBox Learning
     </div>
     <div class="roboto browse-description-threelines grey-4">
      K-8 math games product that adapts to the learner's level of knowledge
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/easytech" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Easy Tech" class="" src="https://edsurge.imgix.net/uploads/product/image/724/Slide1-1459541395.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Easy Tech
     </div>
     <div class="roboto browse-description-threelines grey-4">
      21st century skills curriculum that is delivered through Learning.com's Sky learning platform.
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span>
      ･ 12 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Core Curriculum
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/edgenuity" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-star" title="Product Brief Available">
     <div class="browse-product-card-star-text">
      ★
     </div>
    </div>
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Edgenuity" class="" src="https://edsurge.imgix.net/uploads/product/image/57/edgenuity-1428742514-1428750639.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Edgenuity
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Comprehensive online curriculum for blended learning settings
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/educurious-experiential-learning" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Educurious" class="" src="https://edsurge.imgix.net/uploads/product/image/1037/Educurious-1406914565-1428744040-1428751950.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Educurious
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Learning that connects students to real-world learning
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 6 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/elesapiens-science-fun" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Elesapiens Science &amp; Fun" class="" src="https://edsurge.imgix.net/uploads/product/image/1611/EleScienceFun-1442256945.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Elesapiens Science &amp; Fun
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Interactive science lesson modules in both English and Spanish
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 109 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/espark" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-star" title="Product Brief Available">
     <div class="browse-product-card-star-text">
      ★
     </div>
    </div>
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="eSpark" class="" src="https://edsurge.imgix.net/uploads/product/image/58/espark_logo_200x200-1449873086.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      eSpark
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Develops custom playlists of eBooks, games, videos and learning materials for the iPad
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 24 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/everfi" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="EverFi" class="" src="https://edsurge.imgix.net/uploads/product/image/502/DTAG7g-1484589551.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      EverFi
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Online, gamified courses for 21st Century skills
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 50 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/exibi" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Exibi" class="" src="https://edsurge.imgix.net/uploads/product/image/1381/exibi-1413956227-1428744708-1428752492.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Exibi
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Online portfolio tool for K-12 students
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 11 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/flocabulary" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Flocabulary" class="" src="https://edsurge.imgix.net/uploads/product/image/281/flocabulary-1428742887-1428750936.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Flocabulary
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Educational hip hop songs and videos for current events/core K-12 subjects
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span>
      ･ 89 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/futuremakers-product" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="FutureMakers" class="" src="https://edsurge.imgix.net/uploads/product/image/1494/FutureMakers-1422336278-1428744843-1428752594.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      FutureMakers
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Facilitators of STEAM, project-based lessons
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 93 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/gamesalad-for-education" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="GameSalad for Education" class="" src="https://edsurge.imgix.net/uploads/product/image/2278/bowlboy-1470795890.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      GameSalad for Education
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Curriculum that teaches how to build games
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 25 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/globaloria" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Globaloria" class="" src="https://edsurge.imgix.net/uploads/product/image/698/Globaloria_Square_2-1443657852.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Globaloria
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Blended-learning courses and platform that teach students to design and code educational games
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 80 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/ilit" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="iLIT" class="" src="https://edsurge.imgix.net/uploads/product/image/1380/iLIT-1413951814-1428744699-1428752483.jpeg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      iLIT
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Fosters literacy through personalized reading and learning
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 20 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/immersed-games" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Immersed Games" class="" src="https://edsurge.imgix.net/uploads/product/image/2322/upi4935pt98wxo1pa8zv_400x400-1472853473.jpeg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Immersed Games
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Suite of games for learning ecology
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 7 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/infercabulary" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="InferCabulary" class="" src="https://edsurge.imgix.net/uploads/product/image/1647/InferCabulary-1435685036.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      InferCabulary
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Research-based vocabulary instruction tool that teaches words through analagous visuals
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 32 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/istation-reading" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-star" title="Product Brief Available">
     <div class="browse-product-card-star-text">
      ★
     </div>
    </div>
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Istation Reading" class="" src="https://edsurge.imgix.net/uploads/product/image/65/Istation-1441063447.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Istation Reading
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Research-based curriculum, assessment and intervention program for reading and writing for grades pre-K through 12
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span>
      ･ 23 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/itch" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Itch" class="" src="https://edsurge.imgix.net/uploads/product/image/2257/Slide1-1479439892.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Itch
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Interactive activities and videos for learning Scratch
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 20 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/jumpido-product" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Jumpido" class="" src="https://edsurge.imgix.net/uploads/product/image/1018/Jumpido-1405725013-1428744015-1428751925.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Jumpido
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Series of collaborative and active math games that use the Microsoft Kinect
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 15 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/ket-workplace-essential-skills" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-star" title="Product Brief Available">
     <div class="browse-product-card-star-text">
      ★
     </div>
    </div>
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="KET Workplace Essential Skills" class="" src="https://edsurge.imgix.net/uploads/product/image/1365/KET-1412207266-1428744614-1428752388.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      KET Workplace Essential Skills
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Support adults searching for first-time or better jobs
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/khan-academy" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-star" title="Product Brief Available">
     <div class="browse-product-card-star-text">
      ★
     </div>
    </div>
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Khan Academy" class="" src="https://edsurge.imgix.net/uploads/product/image/29/khanacademy-1428742459-1428750599.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Khan Academy
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Over 5,500 free instructional videos and 100,000 practice exercises on various topics
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/kids-discover-online" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Kids Discover Online" class="" src="https://edsurge.imgix.net/uploads/product/image/1872/FHeob8WJ_400x400-1454096662.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Kids Discover Online
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Library of social studies and science content
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 28 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/koantum-product" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Koantum" class="" src="https://edsurge.imgix.net/uploads/product/image/1725/Koantum_logo-1443049591.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Koantum
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Library of interactive science lessons for grades K-5 designed using the Next Generation Science Standards (NGSS)
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 32 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/kudosreading" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="KudosReading" class="" src="https://edsurge.imgix.net/uploads/product/image/2151/Kudosfb-1484868294.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      KudosReading
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Social Network for kids for reading and playing games
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 18 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/learnbop" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="LearnBop" class="" src="https://edsurge.imgix.net/uploads/product/image/720/lb1-1428743555-1428751515.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      LearnBop
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Automated online math tutoring and analytics tool for K-12 students
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 86 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/learning-bird" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Learning Bird" class="" src="https://edsurge.imgix.net/uploads/product/image/1699/Learning_Bird-1439589421.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Learning Bird
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Library of over 15,000 lessons that enables students to learn a topic through a variety of mediums
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 45 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/lightsail" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="LightSail" class="" src="https://edsurge.imgix.net/uploads/product/image/546/ls_logosquare-1440624338.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      LightSail
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Literacy tool providing standards aligned texts, assessments and data dashboard
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 46 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Core Curriculum
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/listen-current-product" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Listenwise" class="" src="https://edsurge.imgix.net/uploads/product/image/1273/listenwise_FB-1469471152.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Listenwise
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Organized non-fiction, public radio stories covering science, social studies and language arts topics
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 95 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/locomotive-labs-todo-k-2-math-practice" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Todo Math" class="" src="https://edsurge.imgix.net/uploads/product/image/753/todo_logo_200-1442419926.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Todo Math
     </div>
     <div class="roboto browse-description-threelines grey-4">
      CCSS-aligned iOS math games for K - 2 students
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 51 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/logics-academy-product" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Logics Academy" class="" src="https://edsurge.imgix.net/uploads/product/image/1708/Logics_Academy_logo-1440450772.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Logics Academy
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Curriculum-aligned workshops in STEM education for K-12 students by building robotic and aerospace equipment.
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span>
      ･ 39 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/mangahigh" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-star" title="Product Brief Available">
     <div class="browse-product-card-star-text">
      ★
     </div>
    </div>
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Mangahigh" class="" src="https://edsurge.imgix.net/uploads/product/image/25/Logo_-1442417927.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Mangahigh
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Math games and quizzes for grades K -10  with integrated analytics and inter-school competitions
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 31 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/mathgamescom" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="MathGames By TeachMe" class="" src="https://edsurge.imgix.net/uploads/product/image/1938/math_games_by_teachme_main-1477974204.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      MathGames By TeachMe
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Common-core aligned math games for K-8
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 39 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/math-shelf" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Math Shelf" class="" src="https://edsurge.imgix.net/uploads/product/image/2235/Screen_Shot_2016-1470796770.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Math Shelf
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Pre-school and Kindergarten math curriculum for tablets
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span>
      ･ 23 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/mathspace-product" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Mathspace" class="" src="https://edsurge.imgix.net/uploads/product/image/1640/KL1X-1433447756.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Mathspace
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Track and provide feedback on all aspects of a math problem, including intermediate steps
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 151 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Core Curriculum
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/matific" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Matific" class="" src="https://edsurge.imgix.net/uploads/product/image/1029/Copy_of_Logo_-1488089888.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Matific
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Series of math activities and games on the browser and iPad that map to popular textbooks and CCSS
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 177 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/mcgraw-hill-workforce-access" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-star" title="Product Brief Available">
     <div class="browse-product-card-star-text">
      ★
     </div>
    </div>
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="McGraw Hill Workforce Access" class="" src="https://edsurge.imgix.net/uploads/product/image/1385/regular_mhe-education-1414093151-1428744713-1428752496.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      McGraw Hill Workforce Access
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Online courses for adults working toward certifications
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/mcgraw-hill-workforce-connects" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-star" title="Product Brief Available">
     <div class="browse-product-card-star-text">
      ★
     </div>
    </div>
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="McGraw Hill Workforce Connects" class="" src="https://edsurge.imgix.net/uploads/product/image/1384/regular_mhe-education-1414092777-1428744712-1428752495.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      McGraw Hill Workforce Connects
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Supports adult learners in choosing a career path and becoming career-ready
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/mentoring-minds-total-motivation" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Mentoring Minds' Total Motivation" class="" src="https://edsurge.imgix.net/uploads/product/image/2139/iJrfU2ry_400x400-1461967860.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Mentoring Minds' Total Motivation
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Supplemental math &amp; ELA curriculum aligned with Common Core standards
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span>
      ･ 12 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/mindsage-21st-century-skills-program" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="MindSage SEL and MESH Program" class="" src="https://edsurge.imgix.net/uploads/product/image/2173/MINDSAGE_LOGO_Youtube-1464717618.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      MindSage SEL and MESH Program
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Instruction in corporate soft skills for high school students
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 10 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/monster-math" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Monster Math" class="" src="https://edsurge.imgix.net/uploads/product/image/1648/iTunesArtwork-1470368781.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Monster Math
     </div>
     <div class="roboto browse-description-threelines grey-4">
      iPad and iPhone game for K-5 students to practice CCSS-aligned math skills
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 66 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/mosa-mack-science" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Mosa Mack Science" class="" src="https://edsurge.imgix.net/uploads/product/image/878/mosamack_with_character-1428743815-1428751726.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Mosa Mack Science
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Fun science education videos aligned with CCSS and Next Generation Science Standards
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 39 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Core Curriculum
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/motion-math" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Motion Math" class="" src="https://edsurge.imgix.net/uploads/product/image/1/motion_math_logo_white200x200-1442421019.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Motion Math
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Conceptual learning games &amp; dashboard for K-6 math
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 184 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/myblee-math" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="myBlee Math" class="" src="https://edsurge.imgix.net/uploads/product/image/1120/itunesartwork_copy_200x200-1447723798.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      myBlee Math
     </div>
     <div class="roboto browse-description-threelines grey-4">
      iPad app that offers an individualized math learning tool with lessons and exercises students can complete at their own pace
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 22 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Core Curriculum
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/myon-reader" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="myON" class="" src="https://edsurge.imgix.net/uploads/product/image/295/myon_fullcolor_200x200px3-1489709229.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      myON
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Personalized, digitally enhanced literacy and reporting platform for K-8 students
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span>
      ･ 4 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/mystery-science-product" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Mystery Science" class="" src="https://edsurge.imgix.net/uploads/product/image/1379/Mystery_Science-1478887733.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Mystery Science
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Open-and-go lessons that inspire kids to love science.
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 65 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/nepris-industry-connections-platform" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Nepris Industry Connections" class="" src="https://edsurge.imgix.net/uploads/product/image/766/Nepris_New-1412825465-1428743621-1428751579.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Nepris Industry Connections
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Connect teachers and classrooms with subject-relevant STEM professionals
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 116 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/newsela" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-star" title="Product Brief Available">
     <div class="browse-product-card-star-text">
      ★
     </div>
    </div>
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Newsela" class="" src="https://edsurge.imgix.net/uploads/product/image/620/Newsela-1428743423-1428751403.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Newsela
     </div>
     <div class="roboto browse-description-threelines grey-4">
      News stories written to multiple levels of complexity with embedded assessments
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span>
      ･ 149 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/news-o-matic" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="News-O-Matic EDU" class="" src="https://edsurge.imgix.net/uploads/product/image/1030/nom_logo200x200-1442420684.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      News-O-Matic EDU
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Selection of daily news articles for students
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span>
      ･ 127 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/nextlesson-product" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="NextLesson" class="" src="https://edsurge.imgix.net/uploads/product/image/1293/square-1464715788.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      NextLesson
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Standards aligned curriculum, projects, lessons and worksheets for teachers for ELA, Social Studies, Math and Science
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 152 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Core Curriculum
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/noredink" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-star" title="Product Brief Available">
     <div class="browse-product-card-star-text">
      ★
     </div>
    </div>
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="NoRedInk" class="" src="https://edsurge.imgix.net/uploads/product/image/358/nri_logo_square-1503517184.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      NoRedInk
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Teacher-created writing app generates quizzes based on student interests &amp; skill needs
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 19 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/nysci-noticing-tools" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Noticing Tools" class="" src="https://edsurge.imgix.net/uploads/product/image/1135/Slide1-1439502633.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Noticing Tools
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Suite of standards-aligned iOS mobile applications for math and science that promote experiential learning
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 128 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/ooka-island" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Ooka Island" class="" src="https://edsurge.imgix.net/uploads/product/image/1697/OokaIsland_Square-1486003688.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Ooka Island
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Personalized activities and games teaching young students to read
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 39 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/owl-eyes" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Owl Eyes" class="" src="https://edsurge.imgix.net/uploads/product/image/2190/owleyes_logotype__7_-1465595355.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Owl Eyes
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Library of Common core aligned texts for ELA instruction
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 27 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Core Curriculum
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/ponder" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Ponder" class="" src="https://edsurge.imgix.net/uploads/product/image/714/p200x200-1441764593.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Ponder
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Browser add-on that measures reading activity
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 94 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/preptoon" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="PrepToon" class="" src="https://edsurge.imgix.net/uploads/product/image/1854/Preptoon_web-1453230243.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      PrepToon
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Interactive, animated math videos
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 24 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/problemscape" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="ProblemScape" class="" src="https://edsurge.imgix.net/uploads/product/image/1696/PS_LOGO_TR-1440623044.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      ProblemScape
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Multi-platform adventure game that teaches algebra
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 27 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/prodigy" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Prodigy" class="" src="https://edsurge.imgix.net/uploads/product/image/396/Prodigy-1441743345.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Prodigy
     </div>
     <div class="roboto browse-description-threelines grey-4">
      CCSS aligned role-playing math game for grades 1-8.
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span>
      ･ 141 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Core Curriculum
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/propagate-product" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Propagate" class="" src="https://edsurge.imgix.net/uploads/product/image/1023/Propagate-1406581814-1428744022-1428751931.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Propagate
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Browser add-on that tracks and highlights words in any online text and incorporates them into vocab quizzes
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 15 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/pup-s-quest-for-phonics" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Pup's Quest for Phonics" class="" src="https://edsurge.imgix.net/uploads/product/image/777/Pup_s_Quest-1428743635-1428751593.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Pup's Quest for Phonics
     </div>
     <div class="roboto browse-description-threelines grey-4">
      iPad literacy app that teaches one sound at a time.
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 22 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Core Curriculum
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/quill" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Quill" class="" src="https://edsurge.imgix.net/uploads/product/image/738/quill_logo_icon-1453509020.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Quill
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Online exercises that allow students to learn English grammar by writing sentences and proofreading passages.
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 73 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Core Curriculum
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/read-180" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="READ 180" class="" src="https://edsurge.imgix.net/uploads/product/image/506/NtI7RSnh_400x400-1462237910.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      READ 180
     </div>
     <div class="roboto browse-description-threelines grey-4">
      CCSS aligned reading platform for grades 4 to 12, designed for readers below grade level
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 21 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/reading-kingdom" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Reading Kingdom" class="" src="https://edsurge.imgix.net/uploads/product/image/748/Reading_Kingdom-1428743593-1428751551.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Reading Kingdom
     </div>
     <div class="roboto browse-description-threelines grey-4">
      K-3 researched-based, online reading and writing instruction program
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 22 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Core Curriculum
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/readworks" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="ReadWorks" class="" src="https://edsurge.imgix.net/uploads/product/image/732/regular_readworks-1428743570-1428751530.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      ReadWorks
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Online reading comprehension instruction tool that provides strategies and common core aligned lesson plans for teachers.
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 5 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/reasoning-mind" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-star" title="Product Brief Available">
     <div class="browse-product-card-star-text">
      ★
     </div>
    </div>
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Foundations" class="" src="https://edsurge.imgix.net/uploads/product/image/87/rm_logo_200x200-1462294937.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Foundations
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Math program for grades 2-5 based on international standards with training for teachers
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span>
      ･ 11 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/redbird-advanced-learning-courses" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-star" title="Product Brief Available">
     <div class="browse-product-card-star-text">
      ★
     </div>
    </div>
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Redbird Advanced Learning" class="" src="https://edsurge.imgix.net/uploads/product/image/1025/RedBird_Advanced_Learning-1406583459-1428744025-1428751934.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Redbird Advanced Learning
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Adaptive K-12 digital curriculum, blended learning services and professional development
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 41 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/repl-it-classroom" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Repl.It Classroom" class="" src="https://edsurge.imgix.net/uploads/product/image/2323/fvPcCRol_400x400-1472853779.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Repl.It Classroom
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Create &amp;amp; grade coding assignments for students
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 3 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/revision-assistant" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Revision Assistant" class="" src="https://edsurge.imgix.net/uploads/product/image/1915/Revision_Assistant_Logo_Square-1457719382.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Revision Assistant
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Guides students through writing process &amp; provides instant feedback on writing
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 18 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/risu-math" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="RISU Math" class="" src="https://edsurge.imgix.net/uploads/product/image/1859/Logo_200-1452557586.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      RISU Math
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Personalized math curriculum with help from live tutors
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 18 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/roman-town" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Roman Town" class="" src="https://edsurge.imgix.net/uploads/product/image/1496/Roman_Town-1439853095.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Roman Town
     </div>
     <div class="roboto browse-description-threelines grey-4">
      free iPad game in which student practice critical thinking skills while learning about ancient Rome
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 33 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/run-marco" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Run Marco" class="" src="https://edsurge.imgix.net/uploads/product/image/1721/allcancode_logo-1441846480.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Run Marco
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Adventure game to learn coding using visual programming language
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 20 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/scootpad" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="ScootPad" class="" src="https://edsurge.imgix.net/uploads/product/image/206/apple-1492134796.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      ScootPad
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Adaptive platform for K-8 students to practice math and reading skills
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 30 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/scrible-edu" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="scrible Edu" class="" src="https://edsurge.imgix.net/uploads/product/image/459/scrible_s_student_edition_logo_edsurge_summit_application-1442968243.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      scrible Edu
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Save webpages, annotate, share research with peers with added student edition features
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 169 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/shmoop" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Shmoop University" class="" src="https://edsurge.imgix.net/uploads/product/image/208/shmoop2-1428742752-1428750838.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Shmoop University
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Learning resources contextualized with current events &amp; pop culture to appeal to students
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span>
      ･ 2 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/skillsboost" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-star" title="Product Brief Available">
     <div class="browse-product-card-star-text">
      ★
     </div>
    </div>
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Seams LMS" class="" src="https://edsurge.imgix.net/uploads/product/image/1386/seams5-1432511762.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Seams LMS
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Provides online training software programs for companies
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/smallab" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="SMALLab" class="" src="https://edsurge.imgix.net/uploads/product/image/2473/e5cewmmhh4ko57zlfces-1485899422.jpeg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      SMALLab
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Interactive and game-based learning incorporated with the movement of students.
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 3 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/smarter-solving" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Smarter Solving" class="" src="https://edsurge.imgix.net/uploads/product/image/1975/Screen_Shot_2016-1464715867.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Smarter Solving
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Problem solving skills builder for computerized, standardized tests
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 21 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/sofatutor" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Sofatutor" class="" src="https://edsurge.imgix.net/uploads/product/image/361/nacwgh6U_400x400-1459553617.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Sofatutor
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Berlin-based online tutoring platform with videos and personalized tutoring
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 17 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/sokikom" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Sokikom" class="" src="https://edsurge.imgix.net/uploads/product/image/40/gsWYxemI_400x400-1462992826.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Sokikom
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Suite of classroom management tools and adaptive and social math games for grades K-5
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 71 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/solvy-product" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="SOLVY.com" class="" src="https://edsurge.imgix.net/uploads/product/image/1389/Solvy-1414790407-1428744720-1428752501.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      SOLVY.com
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Auto-graded math problems based on real world applications
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 9 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/sown-to-grow" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Sown to Grow" class="" src="https://edsurge.imgix.net/uploads/product/image/2227/Screen_Shot_2016-1486168269.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Sown to Grow
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Goal setting tool for student use
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 92 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/spellnow-year-1" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="SpellNow Series" class="" src="https://edsurge.imgix.net/uploads/product/image/1722/Slide1-1447886832.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      SpellNow Series
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Spelling and vocabulary game for K-4 students
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 32 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/st-math" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-star" title="Product Brief Available">
     <div class="browse-product-card-star-text">
      ★
     </div>
    </div>
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="ST Math" class="" src="https://edsurge.imgix.net/uploads/product/image/26/AppIcon-1459354214.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      ST Math
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Visual, adaptive math program based on neuroscience research from UC Irvine for grades K-7
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/study-island" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-star" title="Product Brief Available">
     <div class="browse-product-card-star-text">
      ★
     </div>
    </div>
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Study Island" class="" src="https://edsurge.imgix.net/uploads/product/image/121/studyisland-1428742607-1428750710.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Study Island
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Standards based individualized practice/ assessment for K-12 core subjects/ test prep
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/successmaker" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-star" title="Product Brief Available">
     <div class="browse-product-card-star-text">
      ★
     </div>
    </div>
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="SuccessMaker" class="" src="https://edsurge.imgix.net/uploads/product/image/83/successmaker-1428742546-1428750665.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      SuccessMaker
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Continuously adaptive reading and math software for grades K-8 providing individualized learning paths
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/swift-csp" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Swift CSP" class="" src="https://edsurge.imgix.net/uploads/product/image/2016/MakeSchool_Diamond_RGB-1458853378.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Swift CSP
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Curriculum for teaching the AP CSP course using Apple Swift
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 36 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/tales2go" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-star" title="Product Brief Available">
     <div class="browse-product-card-star-text">
      ★
     </div>
    </div>
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Tales2go" class="" src="https://edsurge.imgix.net/uploads/product/image/275/Square_smaller-1469471097.jpeg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Tales2go
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Mobile audiobook app delivering on-demand access to thousands of titles from leading publishers and storytellers.
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 78 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/teachermate" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-star" title="Product Brief Available">
     <div class="browse-product-card-star-text">
      ★
     </div>
    </div>
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Teachermate" class="" src="https://edsurge.imgix.net/uploads/product/image/82/teachermate-1428742544-1428750664.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Teachermate
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Online instructional management and software system for K-2 literacy and math. Originally designed for its own handheld system
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/tenmarks" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-star" title="Product Brief Available">
     <div class="browse-product-card-star-text">
      ★
     </div>
    </div>
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="TenMarks Math" class="" src="https://edsurge.imgix.net/uploads/product/image/15/tenmarks-1428742430-1428750580.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      TenMarks Math
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Web-based math program providing lesson plans, curriculum &amp; adaptive practice. Offering curriculum, practice, assessment and intervention for 1st grade - high school
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 13 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/thinkcerca" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="ThinkCERCA" class="" src="https://edsurge.imgix.net/uploads/product/image/549/thinkcerca-1428743337-1428751306.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      ThinkCERCA
     </div>
     <div class="roboto browse-description-threelines grey-4">
      CCSS aligned lessons focused on teaching close reading and argumentative writing across multiple subjects for grades 4 - 12
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 105 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Core Curriculum
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/think-through-math" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-star" title="Product Brief Available">
     <div class="browse-product-card-star-text">
      ★
     </div>
    </div>
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Think Through Math" class="" src="https://edsurge.imgix.net/uploads/product/image/47/TTM_Logo_FULL_COLOR_200_x_200-1446512393.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Think Through Math
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Adaptive math program providing instruction, practice and help from live teachers
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 20 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/thrive-n-shine" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Thrive 'n' Shine" class="" src="https://edsurge.imgix.net/uploads/product/image/1419/Slide1-1416436721-1428744758-1428752538.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Thrive 'n' Shine
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Game teaching financial literacy to teens and young adults
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 3 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/tiggly-product" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Tiggly Education" class="" src="https://edsurge.imgix.net/uploads/product/image/1162/ikz2g-1460594962.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Tiggly Education
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Soft toys interact with iPad learning apps to teach literacy and math to young students
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span>
      ･ 84 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/tilton-s-algebra" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Tilton's Algebra" class="" src="https://edsurge.imgix.net/uploads/product/image/1131/ta_logo200x20002-1453145752.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Tilton's Algebra
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Practice problems and step-by-step help for algebra
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 28 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/time-to-know" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-star" title="Product Brief Available">
     <div class="browse-product-card-star-text">
      ★
     </div>
    </div>
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Time To Know: Teach" class="" src="https://edsurge.imgix.net/uploads/product/image/81/Green_Tree-1470368084.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Time To Know: Teach
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Plan lessons, manage classes and assess performance &amp; progress in real time
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/tinkercad" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Tinkercad" class="" src="https://edsurge.imgix.net/uploads/product/image/1566/Tinkercad_Logo-1427494671-1428745001-1428752693.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Tinkercad
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Browser-based modeling tool for beginners that creates 3D printable designs
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 50 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/turnitin" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Turnitin Feedback Studio" class="" src="https://edsurge.imgix.net/uploads/product/image/252/feedback-1461976927.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Turnitin Feedback Studio
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Plagiarism detection, writing feedback &amp; rubric grading
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 25 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/vidcode-product" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="VidCode" class="" src="https://edsurge.imgix.net/uploads/product/image/1219/Vidcode-1415831288-1428744402-1428752211.jpeg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      VidCode
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Video coding tool aimed to interest girls in coding
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span>
      ･ 16 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/vizwik-product" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Vizwik" class="" src="https://edsurge.imgix.net/uploads/product/image/1718/new-1441403432.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Vizwik
     </div>
     <div class="roboto browse-description-threelines grey-4">
      App development tool for students that does not require previous coding experience
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 18 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/vocabulary-com-product" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Vocabulary.com" class="" src="https://edsurge.imgix.net/uploads/product/image/1556/Vocabularydotcom-1426714651-1428744979-1428752683.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Vocabulary.com
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Online vocabulary building games
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 43 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/vocabularyspellingcity-product" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="VocabularySpellingCity" class="" src="https://edsurge.imgix.net/uploads/product/image/1229/vsc-1472612858.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      VocabularySpellingCity
     </div>
     <div class="roboto browse-description-threelines grey-4">
      A collection of games focused on training students to spell and practice vocabulary
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span>
      ･ 40 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/walkabouts" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Walkabouts" class="" src="https://edsurge.imgix.net/uploads/product/image/2039/Slide1-1458863924.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Walkabouts
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Movement-based video lessons for young learners
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 36 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/word-lab-web" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Word Lab Web" class="" src="https://edsurge.imgix.net/uploads/product/image/1857/Slide1-1454118468.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Word Lab Web
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Learn vocabulary &amp; improve context clue skills from lists of high frequency words
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 40 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/words2learn" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-star" title="Product Brief Available">
     <div class="browse-product-card-star-text">
      ★
     </div>
    </div>
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Words2Learn" class="" src="https://edsurge.imgix.net/uploads/product/image/1304/words2learn-1409952688-1428744533-1428752322.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Words2Learn
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Support adults building vocab skillls
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/words-u" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Words U" class="" src="https://edsurge.imgix.net/uploads/product/image/1746/Word_U_logo-1445381192.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Words U
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Learn college-level words by texting friends
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 17 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/wowzers" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-star" title="Product Brief Available">
     <div class="browse-product-card-star-text">
      ★
     </div>
    </div>
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Wowzers" class="" src="https://edsurge.imgix.net/uploads/product/image/72/wowzers-newlogo-1428742534-1428750654.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Wowzers
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Online learning platform providing story-driven games and activities covering core math curriculum for students in grades 3-5
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/writable" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Writable" class="" src="https://edsurge.imgix.net/uploads/product/image/2405/bmzVmbce-1483830992.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Writable
     </div>
     <div class="roboto browse-description-threelines grey-4">
      A guided practice program to help students enhance writing.
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-half-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 9 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/writereader" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="WriteReader" class="" src="https://edsurge.imgix.net/uploads/product/image/1208/WriteReader_Logo_new_-1444345687.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      WriteReader
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Book creator tool that supports students to learn the basics of reading and writing
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 72 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-2">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/zeal-product" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Zeal" class="" src="https://edsurge.imgix.net/uploads/product/image/1280/z-1462992528.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Zeal
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Online one-to-one math tutoring
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 146 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer present" data-color="1">
     Supplemental
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-0 index-3-0">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/zinc-reading-labs" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Zinc Reading Labs" class="" src="https://edsurge.imgix.net/uploads/product/image/2053/LL_Bar_Ver_S-1459359861.png?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Zinc Reading Labs
     </div>
     <div class="roboto browse-description-threelines grey-4">
      Preparation for college-level reading
     </div>
    </div>
    <div class="browse-product-card-reviews roboto">
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4 produt-star-icon-filled">
      ★
     </span>
     <span class="product-star-icon grey-4">
      ★
     </span>
     <span>
      ･ 19 reviews
     </span>
    </div>
    <div class="roboto grey-4 browse-product-card-footer" data-color="1">
    </div>
   </div>
  </a>
 </li>
 <li class="index-2-1 index-3-1">
  <a class="browse-product-card home mb1" data-color="1" href="/product-reviews/zulama" target="_self">
   <div class="browse-product-card-top-border" data-color="1">
   </div>
   <div class="browse-product-card-rest grey-7" data-color="1">
    <div class="browse-product-card-content pt1 pl1 pr1">
     <div class="mb0_5">
      <img alt="Zulama Entertainment Technology Academy" class="" src="https://edsurge.imgix.net/uploads/product/image/1022/Zulama-1406580866-1428744020-1428751930.jpg?auto=compress%2Cformat&amp;w=100&amp;h=100&amp;fit=crop"/>
     </div>
     <div class="h3 mt0 mb0">
      Zulama Entertainment Technology Academy
     </div>
    </div>
   </div>
  </a>
 </li>
</ul>"
siteText = urlopen(webaddress).read()
soup = BeautifulSoup(siteText, "html.parser")
for products in soup.find_all('div', attrs={"class" : "h3 mt0 mb0"}):
    print (products.text)
"""

soup = BeautifulSoup(siteHTML, "html.parser")
for products in soup.find_all('div', attrs={"class" : "h3 mt0 mb0"}):
    print (products.text)
