import click
from vk.report_friends_info import FriendsReport
from vk.api_vk import VkApi
from writer.writer_json import WriterJson
from writer.writer_csv_tsv import WriterCsvTsv


@click.command()
@click.argument('access_token', type=str)
@click.argument('user_id', type=int)
@click.option('--format_file', '-f',
              type=click.Choice(['csv', 'tsv', 'json']),
              default='csv',
              help='Output file format.')
@click.option('--path', '-p', type=str,
              default=f'./', help='Path to file.')
def main(access_token, user_id, format_file, path) -> None:
    version = '5.131'
    api = VkApi(access_token, version)
    report = FriendsReport(api=api)
    data = report.get_data(user_id)
    data.sort(key=lambda x: x['first_name'])
    writer = object
    if format_file == 'csv':
        writer = WriterCsvTsv(',')
    elif format_file == 'tsv':
        writer = WriterCsvTsv('\t')
    elif format_file == 'json':
        writer = WriterJson(4)
    writer.write(f'{path}report{user_id}.{format_file}', data)
    print(f'Report written to {path}report{user_id}.{format_file}')


if __name__ == '__main__':
    main()
