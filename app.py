from pathlib import Path

import joblib
import pandas as pd
import streamlit as st


APP_ROOT = Path(__file__).parent
LOGO_PATH = APP_ROOT / "lendora_logo.png"
MODEL_PATH = APP_ROOT / "best_model_pipeline.joblib"
PAGES = ("Dashboard", "Loan Assessment", "About Model")


@st.cache_resource(show_spinner=False)
def load_model():
	return joblib.load(MODEL_PATH)


def apply_theme() -> None:
	st.markdown(
		"""
		<style>
		:root {
			--background: #07110D;
			--surface: #0D1A14;
			--green: #22C55E;
			--bright-green: #4ADE80;
			--muted-green: #166534;
			--text: #F0FDF4;
			--secondary: #86A894;
			--border: rgba(134, 168, 148, 0.20);
		}

		.stApp {
			background: var(--background);
			color: var(--text);
		}

		[data-testid="stMainBlockContainer"] {
			max-width: 72rem;
			padding: 3.5rem 3rem 4rem;
		}

		[data-testid="stHeader"] {
			background: transparent;
		}

		#MainMenu, footer {
			visibility: hidden;
		}

		[data-testid="stSidebar"] {
			background: var(--surface);
			border-right: 1px solid var(--border);
		}

		[data-testid="stSidebar"] .block-container {
			padding: 1.8rem 1.25rem 1.5rem;
		}

		.brand-name {
			color: var(--text);
			font-size: 1.2rem;
			font-weight: 700;
			letter-spacing: 0.12em;
			margin: 0.8rem 0 0.2rem;
		}

		.tagline {
			color: var(--secondary);
			font-size: 0.82rem;
			line-height: 1.4;
			margin: 0;
		}

		.eyebrow {
			color: var(--bright-green);
			font-size: 0.75rem;
			font-weight: 700;
			letter-spacing: 0.14em;
			text-transform: uppercase;
			margin: 0;
		}

		.page-title {
			color: var(--text);
			font-size: clamp(2.15rem, 4vw, 3.5rem);
			line-height: 1.05;
			margin: 0.7rem 0 1.1rem;
		}

		.page-subtitle {
			color: var(--secondary);
			font-size: 1.05rem;
			line-height: 1.65;
			max-width: 42rem;
		}

		.section-title {
			color: var(--text);
			font-size: 1rem;
			font-weight: 650;
			margin: 0;
		}

		.section-copy {
			color: var(--secondary);
			font-size: 0.9rem;
			margin: 0.35rem 0 0;
		}

		.metric-label {
			color: var(--secondary);
			font-size: 0.78rem;
			margin-bottom: 0.25rem;
		}

		.metric-value {
			color: var(--text);
			font-size: 1.2rem;
			font-weight: 650;
			margin: 0;
		}

		.status-online {
			color: var(--bright-green);
			font-weight: 650;
		}

		.status-panel {
			border: 1px solid var(--border);
			background: var(--surface);
			padding: 1.15rem;
		}

		.placeholder-panel {
			display: grid;
			grid-template-columns: 3rem 1fr;
			column-gap: 1.2rem;
			align-items: center;
			border-bottom: 1px solid var(--border);
			padding: 1.35rem 0;
		}

		.workflow-number {
			color: var(--bright-green);
			font-size: 0.78rem;
			font-weight: 700;
			letter-spacing: 0.1em;
		}

		.assessment-section-header {
			display: flex;
			align-items: baseline;
			gap: 1.2rem;
			border-bottom: 1px solid var(--border);
			padding-bottom: 1rem;
		}

		.metric-rail {
			display: grid;
			grid-template-columns: repeat(4, 1fr);
			gap: 1.5rem;
			border-top: 1px solid var(--border);
			border-bottom: 1px solid var(--border);
			margin-top: 4.25rem;
			padding: 1.2rem 0;
		}

		.metric-item + .metric-item {
			border-left: 1px solid var(--border);
			padding-left: 1.5rem;
		}

		div.stButton > button {
			border: 1px solid transparent;
			border-radius: 4px;
			color: var(--text);
			background: transparent;
			font-weight: 600;
			min-height: 2.5rem;
			text-align: left;
		}

		div.stButton > button:hover {
			border-color: var(--green);
			color: var(--bright-green);
		}

		div.stButton > button[kind="primary"] {
			background: var(--muted-green);
			border-color: var(--muted-green);
			color: var(--text);
		}

		div.stButton > button[kind="primary"]:hover {
			background: var(--green);
			border-color: var(--green);
			color: var(--text);
		}

		[data-testid="stSidebar"] div.stButton > button {
			justify-content: flex-start;
			padding-left: 0.8rem;
		}

		[data-testid="stSidebar"] div.stButton > button[kind="secondary"]:hover {
			background: rgba(134, 168, 148, 0.08);
		}

		[data-testid="stSidebar"] div.stButton > button[kind="primary"] {
			background: rgba(34, 197, 94, 0.14);
			border-left: 2px solid var(--green);
			border-radius: 0;
			color: var(--bright-green);
		}

		hr {
			border-color: var(--border);
		}

		@media (max-width: 640px) {
			[data-testid="stMainBlockContainer"] {
				padding: 2.5rem 1.25rem 3rem;
			}

			.metric-rail {
				margin-top: 3rem;
				grid-template-columns: repeat(2, 1fr);
			}

			.metric-item + .metric-item {
				border-left: 0;
				padding-left: 0;
			}

			.metric-item:nth-child(n + 3) {
				border-top: 1px solid var(--border);
				padding-top: 0.9rem;
			}
		}

			.result-panel {
				border: 1px solid var(--border);
				background: var(--surface);
				margin-top: 2rem;
				padding: 1.75rem;
			}

			.result-kicker {
				color: var(--bright-green);
				font-size: 0.75rem;
				font-weight: 700;
				letter-spacing: 0.14em;
				margin: 0 0 0.65rem;
				text-transform: uppercase;
			}

			.result-title {
				color: var(--text);
				font-size: 1.8rem;
				font-weight: 700;
				margin: 0;
			}

			.result-copy {
				color: var(--secondary);
				font-size: 0.95rem;
				line-height: 1.55;
				margin: 0.65rem 0 1.6rem;
				max-width: 42rem;
			}

			.probability-row {
				margin-top: 1rem;
			}

			.probability-heading {
				align-items: baseline;
				display: flex;
				justify-content: space-between;
			}

			.probability-label, .probability-value {
				color: var(--text);
				font-size: 0.86rem;
				margin: 0;
			}

			.probability-value {
				color: var(--bright-green);
				font-weight: 700;
			}

			.probability-track {
				background: var(--background);
				height: 0.45rem;
				margin-top: 0.45rem;
				width: 100%;
			}

			.probability-fill {
				background: var(--green);
				height: 100%;
			}

			.disclaimer {
				color: var(--secondary);
				font-size: 0.78rem;
				margin: 1.5rem 0 0;
			}
		</style>
		""",
		unsafe_allow_html=True,
	)


def go_to_page(page: str) -> None:
	st.session_state.current_page = page


def render_sidebar() -> str:
	with st.sidebar:
		if LOGO_PATH.exists():
			st.image(str(LOGO_PATH), width=96)
		st.markdown('<p class="brand-name">LENDORA</p>', unsafe_allow_html=True)
		st.markdown(
			'<p class="tagline">Smarter Lending. Better Decisions.</p>',
			unsafe_allow_html=True,
		)

		st.divider()
		st.markdown('<p class="eyebrow">Navigation</p>', unsafe_allow_html=True)
		current_page = st.session_state.current_page
		for page in PAGES:
			if st.button(
				page,
				key=f"nav_{page.lower().replace(' ', '_')}",
				use_container_width=True,
				type="primary" if current_page == page else "secondary",
			):
				go_to_page(page)
				st.rerun()

		st.divider()
		st.markdown('<p class="eyebrow">Model Status</p>', unsafe_allow_html=True)
		st.markdown(
			'<div class="status-panel">'
			'<p class="status-online">Online</p>'
			'<p class="section-copy">Random Forest</p>'
			'<p class="metric-label" style="margin-top: 1rem;">ROC-AUC</p>'
			'<p class="metric-value">0.9750</p>'
			'</div>',
			unsafe_allow_html=True,
		)
	return st.session_state.current_page


def render_dashboard() -> None:
	st.markdown('<p class="eyebrow">Lendora platform</p>', unsafe_allow_html=True)
	st.markdown(
		'<h1 class="page-title">Smarter Lending.<br>Better Decisions.</h1>',
		unsafe_allow_html=True,
	)
	st.markdown(
		'<p class="page-subtitle">Lendora is a machine-learning-powered loan '
		'assessment application designed to support clear, data-driven lending decisions.</p>',
		unsafe_allow_html=True,
	)
	st.write("")
	if st.button("Start Loan Assessment", type="primary"):
		go_to_page("Loan Assessment")
		st.rerun()

	values = (
		("Model", "Random Forest"),
		("ROC-AUC", "0.9750"),
		("Features", "13"),
		("Status", "Online"),
	)
	metric_items = "".join(
		f'<div class="metric-item"><p class="metric-label">{label}</p>'
		f'<p class="{"status-online" if value == "Online" else "metric-value"}">{value}</p></div>'
		for label, value in values
	)
	st.markdown(f'<div class="metric-rail">{metric_items}</div>', unsafe_allow_html=True)


def render_assessment() -> None:
	st.markdown('<p class="eyebrow">Assessment workspace</p>', unsafe_allow_html=True)
	st.markdown('<h1 class="page-title">Loan Assessment</h1>', unsafe_allow_html=True)
	st.markdown(
		'<p class="page-subtitle">Evaluate loan eligibility using Lendora\'s '
		'machine-learning model.</p>',
		unsafe_allow_html=True,
	)
	st.write("")
	for number, (section, description) in enumerate((
		("Personal Information", "Basic applicant details"),
		("Financial Information", "Provide the applicant's income and requested loan details."),
		("Applicant Profile", "Add employment, education, housing, and loan purpose details."),
		("Credit Information", "Review the applicant's credit history and previous borrowing."),
	), start=1):
		if number == 1:
			st.markdown(
				'<div class="assessment-section-header">'
				f'<span class="workflow-number">{number:02d}</span>'
				f'<p class="section-title">{section}</p>'
				'</div>'
				f'<p class="section-copy">{description}</p>',
				unsafe_allow_html=True,
			)
			age_column, gender_column = st.columns(2)
			with age_column:
				st.number_input("Age", value=0, step=1, format="%d", key="age")
			with gender_column:
				st.selectbox("Gender", options=("female", "male"), key="gender")
			continue

		if number == 2:
			st.markdown(
				'<div class="assessment-section-header">'
				f'<span class="workflow-number">{number:02d}</span>'
				f'<p class="section-title">{section}</p>'
				'</div>'
				f'<p class="section-copy">{description}</p>',
				unsafe_allow_html=True,
			)
			income_column, amount_column = st.columns(2)
			with income_column:
				st.number_input("Annual Income", value=0, step=1, format="%d", key="person_income")
			with amount_column:
				st.number_input("Loan Amount", value=0, step=1, format="%d", key="loan_amount")
			interest_column, percentage_column = st.columns(2)
			with interest_column:
				st.number_input(
					"Loan Interest Rate", value=0.0, step=0.01, format="%.2f", key="loan_interest_rate"
				)
			with percentage_column:
				st.number_input(
					"Loan Percentage", value=0.0, step=0.01, format="%.2f", key="loan_percentage"
				)
			continue

		if number == 3:
			st.markdown(
				'<div class="assessment-section-header">'
				f'<span class="workflow-number">{number:02d}</span>'
				f'<p class="section-title">{section}</p>'
				'</div>'
				f'<p class="section-copy">{description}</p>',
				unsafe_allow_html=True,
			)
			experience_column, education_column = st.columns(2)
			with experience_column:
				st.number_input(
					"Employment Experience", value=0, step=1, format="%d", key="employee_experience"
				)
			with education_column:
				st.selectbox(
					"Education",
					options=("Associate", "Bachelor", "Doctorate", "High School", "Master"),
					key="education",
				)
			home_column, intent_column = st.columns(2)
			with home_column:
				st.selectbox(
					"Home Ownership",
					options=("MORTGAGE", "OTHER", "OWN", "RENT"),
					key="home_onwership",
				)
			with intent_column:
				st.selectbox(
					"Loan Purpose",
					options=(
						"DEBTCONSOLIDATION",
						"EDUCATION",
						"HOMEIMPROVEMENT",
						"MEDICAL",
						"PERSONAL",
						"VENTURE",
					),
					key="loan_intent",
				)
			continue

		if number == 4:
			st.markdown(
				'<div class="assessment-section-header">'
				f'<span class="workflow-number">{number:02d}</span>'
				f'<p class="section-title">{section}</p>'
				'</div>'
				f'<p class="section-copy">{description}</p>',
				unsafe_allow_html=True,
			)
			score_column, history_column = st.columns(2)
			with score_column:
				st.number_input("Credit Score", value=640, step=1, format="%d", key="credit_score")
			with history_column:
				st.number_input("Credit History", value=4, step=1, format="%d", key="credit_history")
			previous_loan_column, _ = st.columns(2)
			with previous_loan_column:
				st.selectbox("Previous Loan", options=("No", "Yes"), key="previous_loan")
			continue

		st.markdown(
			'<div class="placeholder-panel">'
			f'<span class="workflow-number">{number:02d}</span>'
			'<div>'
			f'<p class="section-title">{section}</p>'
			f'<p class="section-copy">{description}</p>'
			'</div>'
			'</div>',
			unsafe_allow_html=True,
		)

	if st.button("Check Eligibility", type="primary", key="check_eligibility"):
		try:
			model = load_model()
		except Exception as error:
			st.error(f"The Lendora model could not be loaded: {error}")
			return

		applicant_values = {
			"age": st.session_state.age,
			"gender": st.session_state.gender,
			"education": st.session_state.education,
			"person_income": st.session_state.person_income,
			"employee_experience": st.session_state.employee_experience,
			"home_onwership": st.session_state.home_onwership,
			"loan_amount": st.session_state.loan_amount,
			"loan_intent": st.session_state.loan_intent,
			"loan_interest_rate": st.session_state.loan_interest_rate,
			"loan_percentage": st.session_state.loan_percentage,
			"credit_history": st.session_state.credit_history,
			"credit_score": st.session_state.credit_score,
			"previous_loan": st.session_state.previous_loan,
		}
		applicant_dataframe = pd.DataFrame([applicant_values])
		expected_columns = list(model.feature_names_in_)
		if list(applicant_dataframe.columns) != expected_columns:
			st.error(
				"The applicant data does not match the model schema. "
				f"Expected {expected_columns}, received {list(applicant_dataframe.columns)}."
			)
			return

		try:
			prediction = int(model.predict(applicant_dataframe)[0])
			classes = list(model.classes_)
			if 0 not in classes or 1 not in classes:
				raise ValueError(f"Unexpected model classes: {classes}")
			probabilities = model.predict_proba(applicant_dataframe)
			if probabilities.shape[0] != 1 or probabilities.shape[1] != len(classes):
				raise ValueError(f"Unexpected probability shape: {probabilities.shape}")
			rejection_probability = float(probabilities[0][classes.index(0)])
			approval_probability = float(probabilities[0][classes.index(1)])
		except Exception as error:
			st.error(f"Eligibility prediction failed: {error}")
			return

		st.session_state.prediction_result = {
			"prediction": prediction,
			"approval_probability": approval_probability,
			"rejection_probability": rejection_probability,
		}

	if "prediction_result" not in st.session_state:
		return

	result = st.session_state.prediction_result
	approved = result["prediction"] == 1
	status = "Loan Approved" if approved else "Loan Not Approved"
	copy = (
		"Based on the information provided, the applicant meets the model's approval criteria."
		if approved
		else "Based on the information provided, the applicant does not meet the model's approval criteria."
	)
	approval_percent = result["approval_probability"] * 100
	rejection_percent = result["rejection_probability"] * 100
	result_html = f"""
	<div class="result-panel">
		<p class="result-kicker">Assessment result</p>
		<p class="result-title">{status}</p>
		<p class="result-copy">{copy}</p>
		<div class="probability-row">
			<div class="probability-heading">
				<p class="probability-label">Approval Probability</p>
				<p class="probability-value">{approval_percent:.1f}%</p>
			</div>
			<div class="probability-track"><div class="probability-fill" style="width: {approval_percent:.6f}%;"></div></div>
		</div>
		<div class="probability-row">
			<div class="probability-heading">
				<p class="probability-label">Rejection Probability</p>
				<p class="probability-value">{rejection_percent:.1f}%</p>
			</div>
			<div class="probability-track"><div class="probability-fill" style="width: {rejection_percent:.6f}%;"></div></div>
		</div>
		<p class="disclaimer">Model prediction only. This result is not a guarantee of loan approval.</p>
	</div>
	"""
	st.markdown(result_html, unsafe_allow_html=True)
	if st.button("Start New Assessment", key="start_new_assessment"):
		del st.session_state.prediction_result
		st.rerun()


def render_about_model() -> None:
	st.markdown('<p class="eyebrow">Model transparency</p>', unsafe_allow_html=True)
	st.markdown('<h1 class="page-title">About Model</h1>', unsafe_allow_html=True)
	st.markdown(
		'<p class="page-subtitle">Lendora uses a Random Forest classifier for binary '
		'loan approval classification.</p>',
		unsafe_allow_html=True,
	)
	st.write("")
	values = (
		("Algorithm", "Random Forest"),
		("ROC-AUC", "0.9750"),
		("Accuracy", "0.9297"),
		("Input Features", "13"),
	)
	metric_items = "".join(
		f'<div class="metric-item"><p class="metric-label">{label}</p>'
		f'<p class="metric-value">{value}</p></div>'
		for label, value in values
	)
	st.markdown(f'<div class="metric-rail">{metric_items}</div>', unsafe_allow_html=True)

	st.divider()
	st.markdown('<p class="section-title">Classification output</p>', unsafe_allow_html=True)
	st.markdown(
		'<p class="section-copy">0 - Loan Rejected<br>1 - Loan Approved</p>',
		unsafe_allow_html=True,
	)
	st.write("")
	st.markdown('<p class="section-title">Pipeline architecture</p>', unsafe_allow_html=True)
	st.markdown(
		'<p class="section-copy">The saved model is a complete preprocessing and '
		'classification pipeline. It supports data-driven assessment but does not '
		'guarantee approval decisions.</p>',
		unsafe_allow_html=True,
	)


def main() -> None:
	st.set_page_config(page_title="Lendora", page_icon="L", layout="wide")
	apply_theme()
	if "current_page" not in st.session_state:
		st.session_state.current_page = "Dashboard"

	page = render_sidebar()
	if page == "Dashboard":
		render_dashboard()
	elif page == "Loan Assessment":
		render_assessment()
	else:
		render_about_model()


if __name__ == "__main__":
	main()
