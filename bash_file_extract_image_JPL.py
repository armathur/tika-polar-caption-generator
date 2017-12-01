import os

with open('/Users/amanmathur/Downloads/type/image-jpeg') as fp:
    lines = fp.read().split("\n")

for i in lines:

    os.system("sshpass -p 'NewPass4u!' scp -r armathur@polar.usc.edu:/data/polar"+ str(i)+" /users/amanmathur/downloads/crawl_data_jpl_img_jpeg/")

