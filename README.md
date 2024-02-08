# Bosch-Computer-Vision-Assignment
This Repository contains the required submissions for the completion of Bosch Computer Vision Assignment.

## 1. Data Analysis
  Data Analysis was performed using two methods.
  <ol>
    <li> Annotation Data Analysis throgh Jupyter Notebook </li>
    <li> Visual Analysis using FiftyOne Tool </li>
  </ol>

### 1. Annotation Data Analysis through Jupyter Notebook

<ul>
  <li>Submission for this Goal  -  "1. BDD_Dataset_Analysis_Notebook.ipynb". The notebook is present is the repository for viewing and evaluation purpose.</li>
  <li>A standalone container is also created to host this notebook environment along with the Dataset.</li>
  <li>How to execute the notebook in a Container.</li>
    <ul>
      <li> Download Docker image</li>
      <li> Create Docker Container </li>
      <li> Start bash and Run jupyter notebook. </li>
      <li> These Notebooks are present in Docker File directories under "BDD100K_Dataset_Analysis" Folder.</li>
    </ul>
</ul>  
      
```shell
docker pull mangeshrc/fiftyone_bdd_repo:latest
docker run --rm -t -d --name=jupyter -p 5000:5000 mangeshrc/fiftyone_bdd_repo:latest
docker exec -ti jupyter bash
jupyter notebook --ip=0.0.0.0 --port=5000 --no-browser --allow-root
```

</ol>
</ol>
