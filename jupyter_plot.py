import sys
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
# 에러출력 무시 모듈
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")
    
# 그래프 바로 출력
# %matplotlib inline

# 작업화면 넓게 조정
# display(HTML("<style>.container { width:90% !important; }</style>"))
    
def plot_bar(df,col):
    """
    데이터프레임의 특정 컬럼으로 groupby 하여 count로 정렬한
    막대그래프 출력

    Args:
        df (dataFrame): 데이터프레임
        col (str): groupby 하고자 하는 컬럼명
    """
    mpl.rc('font',size=12)
    plt.figure(figsize=(20,9))

    ax = sns.countplot(x= col, data=df,
                  palette = sns.color_palette("pastel"),
                  order = df[col].value_counts().iloc[:7].index)

    # countplot에 값 표시
    for p in ax.patches:
        height = p.get_height()
        ax.text(p.get_x() + p.get_width() / 2., height + 30, height, ha = 'center', size = 10)
#     ax.set_ylim(0, ylim)
    plt.show()