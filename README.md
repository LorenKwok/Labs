{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP7TjK5bMtFKC7MX1F4ek5l",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/LorenKwok/Data-Analytics-Using-Python/blob/main/Python_Basics.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"hello\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qlfNkCUn3vTA",
        "outputId": "03c54652-ef14-4e31-f2da-be7552994ca2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "hello\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#python as a calculator\n",
        "print(2+2)\n",
        "print(2-2)\n",
        "print(2*2)\n",
        "print(2/2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DTGSdll0QO2Q",
        "outputId": "0ee83aaa-db90-4485-9f45-69b725d34b87"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4\n",
            "0\n",
            "4\n",
            "1.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# x = 2\n",
        "# 2 + x = ?\n",
        "\n",
        "x = 2\n",
        "print(2+x)\n",
        "\n",
        "#variable declaration\n",
        "\n",
        "mystring = \"I'm a string\"\n",
        "print(mystring)\n",
        "#mystring is a variable\n",
        "\n",
        "#data type - string\n",
        "#strings are defined by their \"\"\n",
        "#strings means words\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CavlCNV6RZRN",
        "outputId": "d99ac25b-338e-4024-ff8a-360c10a5ae78"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4\n",
            "I'm a string\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"2\"+2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 175
        },
        "id": "_k11LWD6THdX",
        "outputId": "84cb9936-0c4b-49eb-e756-3a02e46e7b2e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "TypeError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-8-eeb8e20cf2e6>\u001b[0m in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"2\"\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m: can only concatenate str (not \"int\") to str"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#concatenation - joining strings together\n",
        "\n",
        "partone = \"Hello\"\n",
        "parttwo = \"World\"\n",
        "print(partone + parttwo)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vYTDDgHaSHRA",
        "outputId": "a6974083-b9bd-4d7c-b325-9816859e0de1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "HelloWorld\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#data structures - list\n",
        "#data structure has a container and separators\n",
        "#lists are defined by their []\n",
        "#think of lists as rows in a spreadsheet\n",
        "#a data strucure is a collection of values\n",
        "\n",
        "mylist = [\"1 ROOM\", \"2 ROOM\", \"3 ROOM\", \"4 ROOM\"]\n",
        "#mylist is a list with a collection of 4 strings\n",
        "\n",
        "#query a single value from a list\n",
        "#list have a zero base index\n",
        "#query a single value from a list by its index\n",
        "\n",
        "print(mylist[1])\n",
        "print(mylist[0])\n",
        "\n",
        "#print 4 ROOM\n",
        "print(mylist[3])\n",
        "\n",
        "#query multiple values\n",
        "print(mylist[0:3]) #include:exclude\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "t3Bs0iSVUfoQ",
        "outputId": "f1135dd2-ead8-4917-f652-09b804d71290"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2 ROOM\n",
            "1 ROOM\n",
            "4 ROOM\n",
            "['1 ROOM', '2 ROOM', '3 ROOM']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#data structure - dictionary\n",
        "#dictionaries are defined by its {}\n",
        "#dictionaries are defined by its collection of key:value pairs\n",
        "#think about dictionaries as columns in a spreadsheet\n",
        "\n",
        "mydict = {\"floor_area_sqm\": 56, \"resale_price\": 560000}\n",
        "#mydict is a dictionary with a collection of 2 key:value pairs\n",
        "#the keys are floor_area_sqm and resale_price\n",
        "#the values are 56 and 560000\n",
        "\n",
        "#query a single value from a dictionary with its key\n",
        "print(mydict[\"floor_area_sqm\"])\n",
        "\n",
        "#print 560000\n",
        "print(mydict[\"resale_price\"])\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kJY28jCrbdoC",
        "outputId": "9df5206c-2a13-4aeb-cfd2-4d44a92f9731"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "56\n",
            "560000\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#create a \"table\"\n",
        "\n",
        "house_data = [\n",
        "    {\"town\": \"BEDOK\", \"flat type\": \"3 ROOM\", \"resale_price\": 300000},\n",
        "    {\"town\": \"CHOA CHU KANG\", \"flat_type\": \"4 ROOM\", \"resale_price\": 400000},\n",
        "    {\"town\": \"EAST COAST\", \"flat_type\": \"5 ROOM\", \"resale_price\":500000}\n",
        "]\n",
        "\n",
        "#query a single value\n",
        "print(house_data[0])\n",
        "print(house_data[0][\"town\"])\n",
        "\n",
        "#query 4 ROOM\n",
        "print(house_data[1][\"flat_type\"])\n",
        "\n",
        "#query 500000\n",
        "print(house_data[2][\"resale_price\"])\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3gVF7B1Fe2L0",
        "outputId": "b3b19451-86c7-4a9c-ea6d-10c7fae097f3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'town': 'BEDOK', 'flat type': '3 ROOM', 'resale_price': 300000}\n",
            "BEDOK\n",
            "4 ROOM\n",
            "500000\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "WtRhLQ0FZRLH"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}