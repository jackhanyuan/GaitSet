conf = {
    "WORK_PATH": "./work",
    "CUDA_VISIBLE_DEVICES": "0",
    "data": {
        'dataset_path': "dataset/cut_img",
        'resolution': '64',
        'dataset': 'CASIA-B',
        # In CASIA-B, data of subject #5 is incomplete.
        # Thus, we ignore it in training.
        # For more detail, please refer to
        # function: utils.data_loader.load_data
        'pid_num': 12,  # 训练集人数, 12用于训练, 其余用于测试
        'pid_shuffle': False,
    },
    "model": {
        'hidden_dim': 256,  # 最后一层全连接层的隐藏层数
        'lr': 1e-4,  # 学习率
        'hard_or_full_trip': 'full',
        'batch_size': (8, 16),
        'restore_iter': 0,
        'total_iter': 80000,
        'margin': 0.2,  # 损失函数的margin
        'num_workers': 3,  # 线程数，在windows中请设为0，否则会报错
        'frame_num': 30,  # 每个批次的帧数
        'model_name': 'GaitSet',
    },
}
