import hypothesis.strategies as st
import warnings

if __name__ == '__main__':
    # I ignore some warning, don't worry is all under control!
    # warnings.filterwarnings("ignore")

    # TODO: show some strategy
    strategy = st.lists(st.tuples(st.booleans(), st.integers(min_value=-23, max_value=150)), min_size=0, max_size=500)

    for _ in range(5):
        print(strategy.example())


# def demo_saver():
#    strategy = st.lists(st.integers())

#    strategy = st.lists(
#        st.tuples(
#            st.integers(min_value=0, max_value=5),
#            st.booleans()
#        ),
#        min_size=2, max_size=4
#    )
