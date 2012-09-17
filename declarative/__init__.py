"""

    declarative is a module to create chart class and meta configuration

    example:
    from quickchart.declarative import PieChart
    from quickchart.declarative.store import ModelStore

    class BrowsersStore(ModelStore):
        name = CharField()
        user = ForeingKey('Users')

    class MyPieChart(PieChart):

        data = CountAgregator('name')
        title = 'My Pie Chart'
        store = BrowsersStore()

    m = MyPieChart()
    m.set_resolution(800,600)
    m.save_as_png(file_path)
"""