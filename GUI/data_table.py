from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QDialog
from PyQt5.QtCore import Qt
from Business_Side.file_operations import get_dict_from_json
from Business_Side.plotting import get_pie_chart_by_country
from GUI.button_creator import create_button
from GUI.average_price_prompt import AveragePricePrompt
from GUI.average_score_prompt import AverageScorePrompt
from GUI.country_pie_chart_prompt import CountryPieChartPrompt


class WineEntries(QDialog):
    def __init__(self, data_repo, parent=None):
        self._data_repo = data_repo
        super(WineEntries, self).__init__()
        self.setWindowTitle("Wine Magazine Entries")
        self.setStyleSheet("background-color: gray;")
        self.resize(1200, 800)
        layout = QHBoxLayout()
        layout.addLayout(self._button_sublayout())
        layout.addWidget(self._create_table())
        self.setLayout(layout)

    def _create_table(self):
        table_widget = QTableWidget()
        criteria = get_dict_from_json('criteria.json')['criteria']
        table_widget.setColumnCount(len(criteria))
        table_widget.setHorizontalHeaderLabels(criteria)
        for row in self._data_repo.get_data_from_database(criteria):
            rows = table_widget.rowCount()
            table_widget.setRowCount(rows + 1)
            for i in range(len(criteria)):
                table_widget.setItem(rows, i, QTableWidgetItem(str(row[i])))
        table_widget.resizeColumnsToContents()
        return table_widget

    def _button_sublayout(self):
        criteria = get_dict_from_json('criteria.json')['criteria']
        button_sublayout = QVBoxLayout()
        if 'price' in criteria:
            button_sublayout.addWidget(self._avg_price_button())
        if 'points' in criteria:
            button_sublayout.addWidget(self._avg_points_button())
        if 'country' in criteria:
            button_sublayout.addWidget(self._pie_chart_of_countries_button())
        button_sublayout.addWidget(self._quit_button())
        return button_sublayout

    def _quit_button(self):
        return create_button("Quit Window", self._quit_window_action)

    def _quit_window_action(self):
        self.close()

    def _avg_price_button(self):
        return create_button("Average Price", self._get_avg_price_action)

    def _get_avg_price_action(self):
        AveragePricePrompt(self._data_repo.avg_price()).exec()

    def _avg_points_button(self):
        return create_button("Average Points", self._get_avg_score_action)

    def _get_avg_score_action(self):
        AverageScorePrompt(self._data_repo.avg_points()).exec()

    def _pie_chart_of_countries_button(self):
        return create_button("Country Pie Chart", self._pie_chart_of_countries_action)

    def _pie_chart_of_countries_action(self):
        get_pie_chart_by_country(self._data_repo.get_counts_by_country(self._data_repo.get_list_of_countries()))
        CountryPieChartPrompt().exec()
