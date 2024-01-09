from pre_pull_baseimage import get_pyversion, pull_baseimage, make_dockerfile
import sys

def main():
    print("pythonファイルが保存されました。")
    #versionの取得
    version = get_pyversion.main()

    #pullの実行
    pull_baseimage.main(version)

    #pullしたベースイメージからDockerfileを作成
    make_dockerfile.main(version)

    