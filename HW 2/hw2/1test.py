import experiments
def test11():
    for L in [[32],[64]]:
        for K in [2,4,8,16]:
            experiments.cnn_experiment(
                'test_run', bs_train=50, batches=10, epochs=10, early_stopping=5,
                filters_per_layer=L, layers_per_block=K, pool_every=1, hidden_dims=[100],
                model_type='cnn',checkpoints="checkpoints.txt"
            )


test11()