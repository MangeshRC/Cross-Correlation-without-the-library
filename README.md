# Bosch-Computer-Vision-Assignment
This Repository contains the required submissions for the completion of Bosch Computer Vision Assignment.

## 1. Data Analysis
  Data Analysis was performed using two methods and the analysis document is added to this repository as a PDF file ("Exploratory Data Analysis on BDD100K Dataset.pdf"). 
  <ol>
    <li> Annotation Data Analysis throgh Jupyter Notebook </li>
    <li> Visual Analysis using FiftyOne Tool </li>
  </ol>

##### 1. Annotation Data Analysis through Jupyter Notebook

<ul>
  <li>Submission for this Goal  -  "1. BDD_Dataset_Analysis_Notebook.ipynb". The notebook is present is the repository for viewing and evaluation purpose.</li>
  <li>How to execute the notebook environment in a Container.</li>
    <ul>
      <li> Download Docker image</li>
      <li> Create Docker Container </li>
      <li> Start bash and Run jupyter notebook. </li>
      <li> These Notebooks are present in container File directories under "BDD100K_Dataset_Analysis" Folder.</li>
    </ul>
</ul>  
      
```shell
docker pull mangeshrc/fiftyone_bdd_repo:latest
docker run --rm -t -d --name=jupyter -p 5000:5000 mangeshrc/fiftyone_bdd_repo:latest
docker exec -ti jupyter bash
jupyter notebook --ip=0.0.0.0 --port=5000 --no-browser --allow-root
```

##### 2. Visual Analysis using FiftyOne Tool

<ul>
  <li> Sample Screen for the visualisation tool is as follows:</li>
  
[![fiftyone-screen.png](https://i.postimg.cc/RVDzh390/fiftyone-screen.png)](https://postimg.cc/LnLW08Jd)

  <li>Submission for this Goal  -  "2. Fiftyone_Data_preparation.ipynb" and the </li>
  <li>A standalone container is created to host tool enviornment.</li>
  <li>How to run fiftyone Visualization Tool.</li>
    <ul>
      <li> Download Docker image</li>
      <li> Create Docker Container </li>
      <li> Execute Fiftyone App run file in docker. </li>
    </ul>
</ul>  

```shell
docker pull mangeshrc/fiftyone_bdd_repo:latest
docker run --rm -t -d --name=jupyter -p 5000:5000 mangeshrc/fiftyone_bdd_repo:latest
docker exec -ti jupyter python BDD100K_Dataset_Analysis/fiftyone_run.py
```


## 2. Model

<ul>
  <li>Model inference was obtained using Colab GPU Notebook. A properly formatted code notebook from Colab is added in this repository. ( "3. Colab_Inference_Notebook.ipynb" )</li>
  <li>The execution details are mentioned in the Uploaded Notebook in this repository.</li>
  <li>Few of the Predicted Samples are as follows:</li>

[![Sample-image1.png](https://i.postimg.cc/7LzTS9W4/Sample-image1.png)](https://postimg.cc/VSY68qwZ)

[![Sample-image2.png](https://i.postimg.cc/43pmYdYN/Sample-image2.png)](https://postimg.cc/cK4sjd7V)

</ul>


## 3. Evaluation and Visualization

<ul>
  <li> Model evaluations are derived and uploaded in this repository as a PDF file "Evaluation and Prediction Analysis.pdf" </li>
  <li> Jupyter Notebook used is also uploaded as "4. Prediction_Analysis.ipynb"</li>
  <li> Model evaluations are were computed using Predicted json file from Colab and FiftyOne Tool.</li>
  <li> The visualization for predicted images is not present in the docker image provided. </li>
  <li> These visualizations were performed in local environment. </li>
</ul>

