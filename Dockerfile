FROM sawarae/pirender:0.02
RUN apt install -y unzip less nano
RUN conda install -y  -c conda-forge imageio-ffmpeg pandas packaging
RUN conda install -y -c 1adrianb face_alignment=1.3.6
