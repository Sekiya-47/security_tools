"""
pip install bandit

"""

import bandit
from bandit.core import manager

# スキャン対象のファイル
file_to_scan = 'example.py'

# Banditのマネージャーを初期化
b_mgr = manager.BanditManager(config=None, agg_type='file', debug=False)

# スキャンの実行
b_mgr.run_tests(file_to_scan)

# 結果の表示
for result in b_mgr.results:
    print(result)
