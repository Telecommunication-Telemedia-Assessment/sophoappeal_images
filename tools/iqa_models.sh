#!/bin/bash
# see https://github.com/chaofengc/IQA-PyTorch
pip3 install pyiqa  # (best in a virtenv)
mkdir -p iqa_models
for image_dir in ../*/medium/; do
    db=$(basename $(dirname $image_dir))
    echo $db
    #exit 0
    python3 inference_iqa.py -m NIQE --save_file "iqa_models/$db".NIQE.res -i "$image_dir"
    python3 inference_iqa.py -m MUSIQ --save_file "iqa_models/$db".MUSIQ.res -i "$image_dir"
    #python3 inference_iqa.py -m MANIQA --save_file "iqa_models/$db".MANIQA.res -i "$image_dir"
    python3 inference_iqa.py -m ILNIQE --save_file "iqa_models/$db".ILNIQE.res -i "$image_dir"
    python3 inference_iqa.py -m FID --save_file "iqa_models/$db".FID.res -i "$image_dir"
    python3 inference_iqa.py -m DBCNN --save_file "iqa_models/$db".DBCNN.res -i "$image_dir"
    python3 inference_iqa.py -m BRISQUE --save_file "iqa_models/$db".BRISQUE.res -i "$image_dir"

    # not working
    #python3 inference_iqa.py -m paq2piq --save_file "$db".paq2piq.res -i "stimuli/$db/"
    #python3 inference_iqa.py -m WaDIQaM --save_file "$db".WaDIQaM.res -i "stimuli/$db/"
    #python3 inference_iqa.py -m CNNIQA --save_file "$db".CNNIQA.res -i "stimuli/$db/"
    #python3 inference_iqa.py -m HYPERIQA --save_file "$db".HYPERIQA.res -i "stimuli/$db/"
done

# MUSIQ, HyperIQA, MANIQA
# ['ahiq', 'brisque', 'ckdn', 'cw_ssim', 'dbcnn', 'dists', 'fid', 'fsim', 'gmsd', 'ilniqe', 'lpips', 'lpips-vgg', 'mad', 'maniqa', 'ms_ssim', 'musiq', 'musiq-ava', 'musiq-koniq', 'musiq-paq2piq', 'musiq-spaq', 'nima', 'niqe', 'nlpd', 'nrqm', 'paq2piq', 'pi', 'pieapp', 'psnr', 'ssim', 'vif', 'vsi']
