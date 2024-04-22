(function($) {
	"use strict";
	
	//Canvas
	if ($('#canvas').length) {
		var ctx = document.getElementById("canvas").getContext("2d");

		window.myBar = new Chart(ctx, {
			type: 'bar',
			data: {
				labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
				datasets: [{
					label: 'Dataset 1',
					backgroundColor: "#45beff ",
					borderColor: "#45beff ",
					data: [45, 58, 62, 89, 63, 46, 63]
				}, {
					label: 'Dataset 2',
					backgroundColor: "#8645ff",
					borderColor: "#8645ff",
					data: [25, 55, 64, 9, 30, 96, 33]
				}, {
					label: 'Dataset 3',
					backgroundColor: "#ff8645",
					borderColor: "#ff8645",
					data: [24, 14, 53, 18, 19, 65]
				}]
			},
			options: {

				responsive: true,
				legend: {
					display: false,
					labels: {
						fontColor: "#62617d"
					},
				},

				title: {
					display: false,
					text: 'Chart.js Bar Chart'
				},
				scales: {
					yAxes: [{
						ticks: {
							
							fontColor: "#62617d",
						},
						gridLines: {
							color: 'rgba(161, 161, 161,0.3)'
						}
					}],
					xAxes: [{
						ticks: {
							display: true,
							fontColor: "#62617d",
						},
						gridLines: {
							display: true,
							color: 'rgba(161, 161, 161,0.3)'
						}
					}]
				},
			}
		});
		var resizeId;
	};

	//horizontalbarchart
	if ($('#canvashbar').length) {
		var ctx = document.getElementById("canvashbar").getContext("2d");
		window.myHorizontalBar = new Chart(ctx, {
			type: 'horizontalBar',
			data: {
				labels: ["Jan", "Feb", "Mar", "Apr"],
				datasets: [{
					label: 'Dataset 1',
					backgroundColor: "#45beff ",
					borderColor: '#45beff ',
					data: [45, 58, 62, 89]
				}, {
					label: 'Dataset 2',
					backgroundColor: "#8645ff",
					borderColor: '#8645ff',
					data: [25, 55, 64, 9]
				}, {
					label: 'Dataset 3',
					backgroundColor: "#ff8645",
					borderColor: '#ff8645',
					data: [24, 14, 53, 18]
				}]
			},
			options: {
				elements: {
					rectangle: {
						borderWidth: 2,
						borderColor: 'rgba(255,255,255,0.02)',
						borderSkipped: 'left'
					}
				},
				responsive: true,
				legend: {
					display: false,
					labels: {
						fontColor: "#62617d"
					},
				},
				title: {
					display: false,
					text: 'Chart.js Horizontal Bar Chart'
				},
				scales: {
					yAxes: [{
						ticks: {
							
							fontColor: "#62617d",
						},
						gridLines: {
							color: 'rgba(161, 161, 161,0.3)'
						}
					}],
					xAxes: [{
						ticks: {
							display: true,
							fontColor: "#62617d",
						},
						gridLines: {
							display: true,
							color: 'rgba(161, 161, 161,0.3)'
						}
					}]
				},
			}
		});
	};

	//barchart multix
	if ($('#canvas2').length) {
		var ctx = document.getElementById("canvas2").getContext("2d");
		window.myBar = Chart.Bar(ctx, {
			data: {
				labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
				datasets: [{
					label: 'Dataset 1',
					backgroundColor: "#45beff ",
					borderColor: "#45beff ",
					yAxisID: "y-axis-1",
					data: [14, 18, 25, 36, 54, 42, 52]
				}, {
					label: 'Dataset 2',
					backgroundColor: "#8645ff",
					borderColor: "#8645ff",
					yAxisID: "y-axis-2",
					data: [2, 18, 25, 38, 48, 24, 24]
				}, {
					label: 'Dataset 3',
					backgroundColor: "#ff8645",
					borderColor: "#ff8645",
					yAxisID: "y-axis-1",
					data: [14, 25, 32, 36, 14, 12, 48]
				}]
			},
			options: {
				responsive: true,
				hoverMode: 'label',
				hoverAnimationDuration: 400,
				stacked: false,
				title: {
					display: false,
					text: "Chart.js Bar Chart - Multi Axis"
				},
				legend: {
					display: false,
					labels: {
						fontColor: "#62617d"
					},
					
				},
				scales: {
					yAxes: [{
						type: "linear",
						display: true,
						position: "left",
						id: "y-axis-1",
						ticks: {
						
							fontColor: "#62617d",
						},
						gridLines: {
							color: 'rgba(161, 161, 161,0.3)'
						}
					}, {
						type: "linear",
						display: true,
						position: "right",
						id: "y-axis-2",
						gridLines: {
							drawOnChartArea: false,
							color: 'rgba(161, 161, 161,0.3)'
						},
						ticks: {
						
							fontColor: "#62617d",
						},
						
					}],
					
				}
			}
		});
	};

	//Stacked barchart
	if ($('#canvas3').length) {
		var ctx = document.getElementById("canvas3").getContext("2d");
		window.myBar = new Chart(ctx, {
			type: 'bar',
			data: {
				labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
				datasets: [{
					label: 'Dataset 1',
					backgroundColor: "#45beff ",
					borderColor: "#45beff ",
					data: [14, 25, 32, 36, 14, 12, 48]
				}, {
					label: 'Dataset 2',
					backgroundColor: "#8645ff",
					borderColor: "#8645ff",
					data: [14, 25, 32, 36, 14, 12, 48]
				}, {
					label: 'Dataset 3',
					backgroundColor: "#ff8645",
					borderColor: "#ff8645",
					data: [14, 25, 32, 36, 14, 12, 48]
				}]
			},
			options: {
				title: {
					display: false,
					text: "Chart.js Bar Chart - Stacked"
				},
				tooltips: {
					mode: 'label'
				},
				legend: {
					display: false,
				},
				responsive: true,
				scales: {
					xAxes: [{
						stacked: true,
						ticks: {
						
							fontColor: "#62617d",
						},
						gridLines: {
							color: 'rgba(161, 161, 161,0.3)'
						}
					}],
					yAxes: [{
						stacked: true,
						ticks: {
							
							fontColor: "#62617d",
						},
						gridLines: {
							color: 'rgba(161, 161, 161,0.3)'
						}
					}],
					legend: {
						labels: {
							fontColor: "#62617d"
						},
					},
				}
			}
		});
	};
})(jQuery);