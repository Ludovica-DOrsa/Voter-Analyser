import pandas as pd
import numpy as np


def read_clean_data_plot_1(source = 'ESS-Data-Wizard-subset-2022-12-03.csv'):
    """
    Reads and cleans dataset.
    :param source: position of dataset
    :return:
    """
    df = pd.read_csv(source)
    df['freehms'] = df['freehms'].apply(str)
    df['freehms'] = np.where(df['freehms']=='7', 'No answer', df['freehms'])
    df['freehms'] = np.where(df['freehms']=='8', 'No answer', df['freehms'])
    df['freehms'] = np.where(df['freehms']=='9', 'No answer', df['freehms'])
    df['freehms'] = np.where((df['freehms']=='1')|(df['freehms']=='2'), 'Agree', df['freehms'])
    df['freehms'] = np.where((df['freehms']=='3'), 'Neither agree nor disagree', df['freehms'])
    df['freehms'] = np.where((df['freehms']=='4')|(df['freehms']=='5'), 'Disagree', df['freehms'])

    df['gndr'] = df['gndr'].apply(str)
    df['gndr'] = np.where((df['gndr']=='1'), 'Male', df['gndr'])
    df['gndr'] = np.where((df['gndr']=='2'), 'Female', df['gndr'])
    df['gndr'] = np.where((df['gndr']=='9'), 'No answer', df['gndr'])

    df['mnrgtjb'] = df['mnrgtjb'].apply(str)
    df['mnrgtjb'] = np.where((df['mnrgtjb']=='1.0')|(df['mnrgtjb']=='2.0'), 'Agree', df['mnrgtjb'])
    df['mnrgtjb'] = np.where((df['mnrgtjb']=='3.0'), 'Neither agree nor disagree', df['mnrgtjb'])
    df['mnrgtjb'] = np.where((df['mnrgtjb']=='4.0')|(df['mnrgtjb']=='5.0'), 'Disagree', df['mnrgtjb'])
    df['mnrgtjb'] = np.where((df['mnrgtjb']=='7.0')|(df['mnrgtjb']=='8.0')|(df['mnrgtjb']=='9.0'), 'No answer', df['mnrgtjb'])

    df['ccnthum'] = df['ccnthum'].apply(str)
    df['ccnthum'] = np.where((df['ccnthum']=='1.0')|(df['ccnthum']=='2.0'), 'Natural processes', df['ccnthum'])
    df['ccnthum'] = np.where((df['ccnthum']=='3.0'), 'Both', df['ccnthum'])
    df['ccnthum'] = np.where((df['ccnthum']=='4.0')|(df['ccnthum']=='5.0'), 'Human activity', df['ccnthum'])
    df['ccnthum'] = np.where((df['ccnthum']=='55.0'), 'Climate change not happening', df['ccnthum'])
    df['ccnthum'] = np.where((df['ccnthum']=='66.0')|(df['ccnthum']=='77.0')|(df['ccnthum']=='88.0')|(df['ccnthum']=='99.0'),
                         'Climate change not happening', df['ccnthum'])

    df['edlvit'] = df['edlvit'].apply(str)
    df['edlvit'] = np.where((df['edlvit']=='3.0')|(df['edlvit']=='1.0')|(df['edlvit']=='2.0'), 'Middle school or lower', df['edlvit'])
    df['edlvit'] = np.where((df['edlvit']=='4.0'), 'High school', df['edlvit'])
    df['edlvit'] = np.where((df['edlvit']=='5.0'), 'University diploma', df['edlvit'])
    df['edlvit'] = np.where((df['edlvit']=='6.0'), 'University degree', df['edlvit'])
    df['edlvit'] = np.where((df['edlvit']=='7.0'), 'Post-degree specialisation', df['edlvit'])
    df['edlvit'] = np.where((df['edlvit']=='8.0')|(df['edlvit']=='77.0')|(df['edlvit']=='88.0')
                        |(df['edlvit']=='99.0'), 'Post-degree specialisation', df['edlvit'])

    df['edulvla'] = df['edulvla'].apply(str)
    df['edulvla'] = np.where((df['edulvla'] == '1.0'), 'Less than lower secondary', df['edulvla'])
    df['edulvla'] = np.where((df['edulvla'] == '2.0'), 'Lower secondary', df['edulvla'])
    df['edulvla'] = np.where((df['edulvla'] == '3.0'), 'Upper secondary', df['edulvla'])
    df['edulvla'] = np.where((df['edulvla'] == '4.0'), 'Post-secondary non-tertiary', df['edulvla'])
    df['edulvla'] = np.where((df['edulvla'] == '5.0'), 'Tertiary', df['edulvla'])
    df['edulvla'] = np.where((df['edulvla'] == '0.0')|(df['edulvla'] == '55.0')|
                             (df['edulvla'] == '77.0')|(df['edulvla'] == '88.0')|
                             (df['edulvla'] == '0.0')|(df['edulvla'] == '99.0')
                             |(df['edulvla'] == 'nan'), np.NAN, df['edulvla'])



    df['emplrel'] = df['emplrel'].apply(str)
    df['emplrel'] = np.where((df['emplrel']=='1'), 'Employee', df['emplrel'])
    df['emplrel'] = np.where((df['emplrel']=='2'), 'Self-employed', df['emplrel'])
    df['emplrel'] = np.where((df['emplrel']=='3'), 'Working for own family business', df['emplrel'])
    df['emplrel'] = np.where((df['emplrel']=='6')|(df['emplrel']=='7')|(df['emplrel']=='8')|(df['emplrel']=='9'),
                         'No answer', df['emplrel'])

    df['marital'] = df['marital'].apply(str)
    df['marital'] = np.where((df['marital']=='1.0')|(df['marital']=='4.0'), 'Married or widowed', df['marital'])
    df['marital'] = np.where((df['marital']=='2.0')|(df['marital']=='3.0'), 'Separated or divorced', df['marital'])
    df['marital'] = np.where((df['marital']=='5.0'), 'Never married', df['marital'])
    df['marital'] = np.where((df['marital']=='7.0')|(df['marital']=='8.0')|(df['marital']=='9.0'), 'No answer', df['marital'])

    df['party'] = np.NAN
    # 1 = 'Partido Democratico'
    df['party'] = np.where((df['prtclbit'] == 1)|(df['prtclcit']== 2) | (df['prtcldit']== 1), 0.1, df['party'])
    # 2 = Movimento 5 Stelle
    df['party'] = np.where((df['prtclbit'] == 3) | (df['prtclcit'] == 1) | (df['prtcldit'] == 7), 0.2, df['party'])
    # 3 = Lega Nord
    df['party'] = np.where((df['prtclbit'] == 9) | (df['prtclcit'] == 3) | (df['prtcldit'] == 9), 0.3, df['party'])
    # 4 = Fratelli d'Italia
    df['party'] = np.where((df['prtclbit'] == 10) | (df['prtclcit'] == 5) | (df['prtcldit'] == 10), 0.4, df['party'])
    # 5 = Forza Italia - PdL
    df['party'] = np.where((df['prtclbit'] == 8) | (df['prtclcit'] == 4) | (df['prtcldit'] == 8), 0.5, df['party'])
    # 6 = Other
    df['party'] = np.where((df['prtclbit'] == 2) | (df['prtclbit'] == 3) | (df['prtclbit'] == 5) | (df['prtclbit'] == 6)
                           | (df['prtclbit'] == 7) | (df['prtclbit'] == 11) | (df['prtclbit'] == 12)
                           | (df['prtclbit'] == 13) | (df['prtclbit'] == 14) |

                           (df['prtclcit'] == 6) | (df['prtclcit'] == 7) | (df['prtclcit'] == 8) | (df['prtclcit'] == 9) |

                           (df['prtcldit'] == 2) | (df['prtcldit'] == 3) | (df['prtcldit'] == 4) | (df['prtcldit'] == 5) |
                           (df['prtcldit'] == 6) | (df['prtcldit'] == 11) | (df['prtcldit'] == 12) | (df['prtcldit'] == 13) |
                           (df['prtcldit'] == 14),
                           0.6, df['party'])
    # 9 = No answer
    df['party'] = np.where((df['prtclbit'] == 66) | (df['prtclbit'] == 77) | (df['prtclbit'] == 88) | (df['prtclbit'] == 99) |
                           (df['prtclcit'] == 66) | (df['prtclcit'] == 77) | (df['prtclcit'] == 88) | (df['prtclcit'] == 99) |
                           (df['prtcldit'] == 66) | (df['prtcldit'] == 77) | (df['prtcldit'] == 88) | (df['prtcldit'] == 99)
                           , 0.9, df['party'])

    df = df[df['party'].notna()]
    df = df[df['freehms'].notna()]

    df = df[df['ccnthum'].notna()]
    df = df[df['mnrgtjb'].notna()]
    df = df[df['party']!=0.9]
    df = df[df['ccnthum'] != 'nan']
    df = df[df['mnrgtjb'] != 'nan']

    return df


def read_clean_data_plot_2(source = 'ESS-Data-Wizard-subset-2022-12-03.csv'):

    df = pd.read_csv(source)
    df['party'] = np.NAN
    # 1 = 'Partito Democratico'
    df['party'] = np.where((df['prtclbit'] == 1) | (df['prtclcit'] == 2) | (df['prtcldit'] == 1), 0.1, df['party'])
    # 2 = Movimento 5 Stelle
    df['party'] = np.where((df['prtclbit'] == 3) | (df['prtclcit'] == 1) | (df['prtcldit'] == 7), 0.2, df['party'])
    # 3 = Lega Nord
    df['party'] = np.where((df['prtclbit'] == 9) | (df['prtclcit'] == 3) | (df['prtcldit'] == 9), 0.3, df['party'])
    # 4 = Fratelli d'Italia
    df['party'] = np.where((df['prtclbit'] == 10) | (df['prtclcit'] == 5) | (df['prtcldit'] == 10), 0.4, df['party'])
    # 5 = Forza Italia - PdL
    df['party'] = np.where((df['prtclbit'] == 8) | (df['prtclcit'] == 4) | (df['prtcldit'] == 8), 0.5, df['party'])
    # 6 = Other
    df['party'] = np.where((df['prtclbit'] == 2) | (df['prtclbit'] == 3) | (df['prtclbit'] == 5) | (df['prtclbit'] == 6)
                           | (df['prtclbit'] == 7) | (df['prtclbit'] == 11) | (df['prtclbit'] == 12)
                           | (df['prtclbit'] == 13) | (df['prtclbit'] == 14) |

                           (df['prtclcit'] == 6) | (df['prtclcit'] == 7) | (df['prtclcit'] == 8) | (
                                       df['prtclcit'] == 9) |

                           (df['prtcldit'] == 2) | (df['prtcldit'] == 3) | (df['prtcldit'] == 4) | (
                                       df['prtcldit'] == 5) |
                           (df['prtcldit'] == 6) | (df['prtcldit'] == 11) | (df['prtcldit'] == 12) | (
                                       df['prtcldit'] == 13) |
                           (df['prtcldit'] == 14),
                           0.6, df['party'])
    # 9 = No answer
    df['party'] = np.where(
        (df['prtclbit'] == 66) | (df['prtclbit'] == 77) | (df['prtclbit'] == 88) | (df['prtclbit'] == 99) |
        (df['prtclcit'] == 66) | (df['prtclcit'] == 77) | (df['prtclcit'] == 88) | (df['prtclcit'] == 99) |
        (df['prtcldit'] == 66) | (df['prtcldit'] == 77) | (df['prtcldit'] == 88) | (df['prtcldit'] == 99)
        , 0.9, df['party'])

    df['agea'] = np.where(df['agea']==999, np.NAN, df['agea'])

    df = df[df['party'].notna()]

    return df

def read_clean_data_plot_3(d_value):
    df = read_clean_data_plot_2()
    party_dict = {0.1: "Partito Democratico",
                    0.2: "Movimento 5 Stelle",
                    0.3: "Lega Nord",
                    0.4: "Fratelli d'Italia",
                    0.5: "Forza Italia - PdL"}

    df["party_name"] = df["party"].map(party_dict)
    df = df[[d_value, 'agea', 'party_name']]
    df = df[(df[d_value] != 77) & (df[d_value] != 88) & (df[d_value] != 99)]
    return df



def read_clean_data_plot_4(source = 'ESS-Data-Wizard-subset-2022-12-03.csv'):
    """
    Reads and cleans dataset.
    :param source: position of dataset
    :return:
    """
    df = pd.read_csv(source)


    df['gndr'] = df['gndr'].apply(str)
    df['gndr'] = np.where((df['gndr']=='1'), 'Male', df['gndr'])
    df['gndr'] = np.where((df['gndr']=='2'), 'Female', df['gndr'])
    df['gndr'] = np.where((df['gndr']=='9'), 'No answer', df['gndr'])

    df['edulvla'] = df['edulvla'].apply(str)
    df['edulvla'] = np.where((df['edulvla'] == '1.0'), 'Less than lower secondary', df['edulvla'])
    df['edulvla'] = np.where((df['edulvla'] == '2.0'), 'Lower secondary', df['edulvla'])
    df['edulvla'] = np.where((df['edulvla'] == '3.0'), 'Upper secondary', df['edulvla'])
    df['edulvla'] = np.where((df['edulvla'] == '4.0'), 'Post-secondary non-tertiary', df['edulvla'])
    df['edulvla'] = np.where((df['edulvla'] == '5.0'), 'Tertiary', df['edulvla'])
    df['edulvla'] = np.where((df['edulvla'] == '0.0')|(df['edulvla'] == '55.0')|
                             (df['edulvla'] == '77.0')|(df['edulvla'] == '88.0')|
                             (df['edulvla'] == '0.0')|(df['edulvla'] == '99.0')
                             |(df['edulvla'] == 'nan'), np.NAN, df['edulvla'])

    df['emplrel'] = df['emplrel'].apply(str)
    df['emplrel'] = np.where((df['emplrel']=='1'), 'Employee', df['emplrel'])
    df['emplrel'] = np.where((df['emplrel']=='2'), 'Self-employed', df['emplrel'])
    df['emplrel'] = np.where((df['emplrel']=='3'), 'Working for own family business', df['emplrel'])
    df['emplrel'] = np.where((df['emplrel']=='6')|(df['emplrel']=='7')|(df['emplrel']=='8')|(df['emplrel']=='9'),
                         'No answer', df['emplrel'])

    df['party'] = np.NAN
    # 1 = 'Partido Democratico'
    df['party'] = np.where((df['prtclbit'] == 1)|(df['prtclcit']== 2) | (df['prtcldit']== 1), 0.1, df['party'])
    # 2 = Movimento 5 Stelle
    df['party'] = np.where((df['prtclbit'] == 3) | (df['prtclcit'] == 1) | (df['prtcldit'] == 7), 0.2, df['party'])
    # 3 = Lega Nord
    df['party'] = np.where((df['prtclbit'] == 9) | (df['prtclcit'] == 3) | (df['prtcldit'] == 9), 0.3, df['party'])
    # 4 = Fratelli d'Italia
    df['party'] = np.where((df['prtclbit'] == 10) | (df['prtclcit'] == 5) | (df['prtcldit'] == 10), 0.4, df['party'])
    # 5 = Forza Italia - PdL
    df['party'] = np.where((df['prtclbit'] == 8) | (df['prtclcit'] == 4) | (df['prtcldit'] == 8), 0.5, df['party'])
    # 6 = Other
    df['party'] = np.where((df['prtclbit'] == 2) | (df['prtclbit'] == 3) | (df['prtclbit'] == 5) | (df['prtclbit'] == 6)
                           | (df['prtclbit'] == 7) | (df['prtclbit'] == 11) | (df['prtclbit'] == 12)
                           | (df['prtclbit'] == 13) | (df['prtclbit'] == 14) |

                           (df['prtclcit'] == 6) | (df['prtclcit'] == 7) | (df['prtclcit'] == 8) | (df['prtclcit'] == 9) |

                           (df['prtcldit'] == 2) | (df['prtcldit'] == 3) | (df['prtcldit'] == 4) | (df['prtcldit'] == 5) |
                           (df['prtcldit'] == 6) | (df['prtcldit'] == 11) | (df['prtcldit'] == 12) | (df['prtcldit'] == 13) |
                           (df['prtcldit'] == 14),
                           0.6, df['party'])
    # 9 = No answer
    df['party'] = np.where((df['prtclbit'] == 66) | (df['prtclbit'] == 77) | (df['prtclbit'] == 88) | (df['prtclbit'] == 99) |
                           (df['prtclcit'] == 66) | (df['prtclcit'] == 77) | (df['prtclcit'] == 88) | (df['prtclcit'] == 99) |
                           (df['prtcldit'] == 66) | (df['prtcldit'] == 77) | (df['prtcldit'] == 88) | (df['prtcldit'] == 99)
                           , 0.9, df['party'])

    df = df[df['party'].notna()]
    df = df[df['party']!=0.9]

    return df


def read_clean_data_plot_5(source='ESS-Data-Wizard-subset-2022-12-03.csv'):

    df = pd.read_csv(source)

    df['lrscale'] = np.where((df['lrscale']==77)|(df['lrscale']==88)|(df['lrscale']==99), np.NAN, df['lrscale'])


    region_dict = {1.0: "Piemonte",
                   2.0: "Valle d'Aosta/Vallée d'Aoste",
                   3.0: "Lombardia",
                   4.0: "Trentino-Alto Adige/Südtirol",
                   5.0: "Veneto",
                   6.0: "Friuli-Venezia Giulia",
                   7.0: "Liguria",
                   8.0: "Emilia-Romagna",
                   9.0: "Toscana",
                   10.0: "Umbria",
                   11.0: "Marche",
                   12.0: "Lazio",
                   13.0: "Abruzzo",
                   14.0: "Molise",
                   15.0: "Campania",
                   16.0: "Puglia",
                   17.0: "Basilicata",
                   18.0: "Calabria",
                   19.0: "Sicilia",
                   20.0: "Sardegna",
                   999.0: np.NaN
                   }

    df["reg_name"] = df["regionit"].map(region_dict)

    df = df[['reg_name', 'lrscale']]

    df = df.groupby(['reg_name'])['lrscale'].mean().reset_index()

    return df






